import re, json, sys
from collections import defaultdict, OrderedDict
from parse_cns import parse_cns

# See parse_cns.py's own note (same file this script imports from) for the character
# height-clamp rule (180-200 world px, measured from each character's own idle sprite, enforced
# automatically by lite-fighter.html) - this script, like parse_cns.py, only ever deals with
# state/controller data, never sprite scale, so there's nothing size-related to do here either.

def build_statedefs(sections):
    """Groups sections into {statedef_num: {'name':..., 'body':[...], 'controllers':[{'header':..,'type':..,'params':{...}}]}}"""
    statedefs = OrderedDict()
    cur_num = None
    for s in sections:
        header = s['header']
        low = header.lower()
        if low.startswith('statedef'):
            m = re.match(r'statedef\s+(-?\d+)\s*(?:,\s*(.*))?', low)
            if not m:
                cur_num = None
                continue
            num = int(m.group(1))
            name = header.split(',', 1)[1].strip() if ',' in header else ''
            cur_num = num
            statedefs[num] = {'name': name, 'body': dict(s['body']), 'controllers': []}
        elif low.startswith('state'):
            if cur_num is None:
                continue
            # collapse duplicate keys (trigger1/trigger2/..) into lists under one dict, but also keep raw list
            params = {}
            for k, v in s['body']:
                if k in params:
                    if not isinstance(params[k], list):
                        params[k] = [params[k]]
                    params[k].append(v)
                else:
                    params[k] = v
            ctrl_type = params.get('type', '')
            statedefs[cur_num]['controllers'].append({'header': header, 'type': ctrl_type, 'params': params})
    return statedefs

if __name__ == '__main__':
    path = sys.argv[1]
    sections = parse_cns(path)
    sd = build_statedefs(sections)
    print(f"{len(sd)} statedefs found")
    nums = sorted(sd.keys())
    print(nums[:50])
