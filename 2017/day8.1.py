var = {}


def parse_line(line):
    return [val.strip() for val in line.split(' ')]


def should_add_val(val):
    return {
        '==': lambda x: var[x[0]] == int(x[2]),
        '!=': lambda x: var[x[0]] != int(x[2]),
        '<=': lambda x: var[x[0]] <= int(x[2]),
        '>=': lambda x: var[x[0]] >= int(x[2]),
        '>': lambda x: var[x[0]] > int(x[2]),
        '<': lambda x: var[x[0]] < int(x[2]),
    }[val[1]](val)


def add_val(val):
    return {
        'inc': lambda x: var[x[0]] + int(x[2]),
        'dec': lambda x: var[x[0]] - int(x[2])
    }[val[1]](val)


high = 0
with open('day8.txt', 'r') as f:
    for line in f:
        val = parse_line(line)
        if val[0] not in var:
            var[val[0]] = 0

        if val[4] not in var:
            var[val[4]] = 0

        if should_add_val(val[4:]):
            x = add_val(val[:3])
            var[val[0]] = x
            if x > high:
                high = x

maximum = max(var, key=var.get)
print(maximum, var[maximum])
print(high)
