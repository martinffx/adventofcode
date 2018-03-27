with open('day16.txt', 'r') as f:
    moves = f.readline().split(',')


def spin(programs, a):
    idx = len(programs) - a
    return programs[idx:] + programs[:idx]


def exchange(programs, a, b):
    val_a, val_b = programs[a], programs[b]
    programs[a], programs[b] = val_b, val_a
    return programs


def partner(programs, a, b):
    idx_a, idx_b = programs.index(a), programs.index(b)
    programs[idx_b], programs[idx_a] = a, b
    return programs


def one(moves):
    programs = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p'
    ]

    if len(programs) < 16:
        raise Exception('INPUTQ')

    for move in moves:
        if move[0] == 's':
            programs = spin(programs, int(move[1:]))
            continue

        if move[0] == 'x':
            a, b = move[1:].split('/')
            programs = exchange(programs, int(a), int(b))
            continue

        if move[0] == 'p':
            programs = partner(programs, move[1], move[3])
            continue

        raise Exception("Unknown Move!")
    return ''.join(programs)


def two(moves):
    programs = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p'
    ]

    if len(programs) < 16:
        raise Exception('INPUTQ')

    count = 0
    while count < 1000000000:
        for move in moves:
            if move[0] == 's':
                programs = spin(programs, int(move[1:]))
                continue

            if move[0] == 'x':
                a, b = move[1:].split('/')
                programs = exchange(programs, int(a), int(b))
                continue

            if move[0] == 'p':
                programs = partner(programs, move[1], move[3])
                continue

            raise Exception("Unknown Move!")
        count += 1

    return ''.join(programs)


print('TEST', partner(
    exchange(spin(['a', 'b', 'c', 'd', 'e'], 1), 3, 4), 'e', 'b'))
print("A", one(moves))
print("B", two(moves))
