with open('day7.txt', 'r') as f:
    lines = f.readlines()


def parse_line(line):
    x = line.split('->')
    key = x[0].split(' ')
    if len(x) == 1:
        return {'key': key[0], 'value': key[1]}

    child = [v.strip() for v in x[1].split(', ')]
    return {
        'key': key[0],
        'value': int(key[1].strip('(').strip(')')),
        'child': child
    }


tree = {}
parent = {}
for line in lines:
    x = parse_line(line)

    if x['key'] in tree:
        raise Exception('HELP!')

    tree[x['key']] = x
    if 'child' in x:
        for child in x['child']:
            parent[child] = x['key']

res = {}
for k, v in tree.items():
    if k not in parent:
        print(k)

    if 'child' not in v:
        res[k] = v
        continue

    v['children'] = [tree[child_key] for child_key in v['child']]
    res[k] = v
