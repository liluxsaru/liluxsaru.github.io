import re, json, sys
from collections import defaultdict

# NOTE for anyone parsing a new character's raw MUGEN files with this script: this tool only
# extracts state/controller data (moves, hitboxes, etc.) - it does NOT touch sprite scale/size.
# Every playable character's on-screen height is measured and clamped automatically by the game
# itself (lite-fighter.html - see the CHARACTER_MIN_HEIGHT_PX/CHARACTER_MAX_HEIGHT_PX comment
# block there, near where the old SIZE_SCALE table used to live): each character's own idle-pose
# sprite height (spr_off_y, straight from its sprite_atlas_<name>.csv) is measured at load time and
# scaled so the character renders between 180 and 200 world px tall, proportionally - a
# character's own idle sprite mostly just decides HOW CLOSE to the 200 ceiling it lands (anything
# with modest native art clamps straight up to the 180 floor), never below 180 or above 200. A newly
# added character needs NO manual size entry anywhere for this to work correctly; it just needs a
# real idle animation (action 0, or whatever poseMap.idle resolves to) with a normal standing frame
# for the measurement to be meaningful.

def parse_cns(path):
    """Parses a MUGEN .cns/.cmd file into a list of sections, each:
       {header: 'Statedef 200' or 'State 0, Name', body: [(key, value), ...]}
    """
    with open(path, 'r', encoding='latin-1') as f:
        text = f.read()
    lines = text.split('\n')
    sections = []
    cur = None
    for raw in lines:
        line = raw.strip('\r\n')
        # strip comments (semicolon not inside quotes) - simple heuristic: find ';' outside quotes
        out = []
        in_quotes = False
        for ch in line:
            if ch == '"':
                in_quotes = not in_quotes
            if ch == ';' and not in_quotes:
                break
            out.append(ch)
        line = ''.join(out).rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('[') and stripped.endswith(']'):
            if cur is not None:
                sections.append(cur)
            cur = {'header': stripped[1:-1].strip(), 'body': []}
        else:
            if cur is None:
                continue
            if '=' in stripped:
                k, v = stripped.split('=', 1)
                cur['body'].append((k.strip().lower(), v.strip()))
            else:
                cur['body'].append((stripped.lower(), ''))
    if cur is not None:
        sections.append(cur)
    return sections

if __name__ == '__main__':
    path = sys.argv[1]
    sections = parse_cns(path)
    print(f"{len(sections)} sections")
    # print unique header prefixes
    kinds = defaultdict(int)
    for s in sections:
        kind = s['header'].split(',')[0].split(' ')[0]
        kinds[kind] += 1
    for k, v in sorted(kinds.items()):
        print(k, v)
