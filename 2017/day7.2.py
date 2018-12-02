with open('day7.txt', 'r') as f:
    lines = f.readlines()


def parse_line(line):
    x = line.split('->')
    key = x[0].split(' ')
    if len(x) == 1:
        return {
            'key': key[0],
            'value': int(key[1].strip().strip('(').strip(')'))
        }

    child = [v.strip() for v in x[1].split(', ')]
    return {
        'key': key[0],
        'value': int(key[1].strip('(').strip(')')),
        'child': child
    }


def balanced_weight(node, tree):
    if 'child' not in node:
        return node['value']

    children = [tree[child] for child in node['child']]
    weights = [balanced_weight(child, tree) for child in children]
    if all([weights[0] == weight for weight in weights]):
        return node['value'] + sum(weights)

    print(children)
    print(node['child'])
    print(weights)
    raise Exception('Help!')


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

root = tree['ykpsek']
balanced_weight(root, tree)
