from itertools import cycle


def move_right(pos):
    return pos[0] + 1, pos[1]


def move_down(pos):
    return pos[0], pos[1] - 1


def move_left(pos):
    return pos[0] - 1, pos[1]


def move_up(pos):
    return pos[0], pos[1] + 1


res = []


def spiral(end):
    moves = [move_right, move_down, move_left, move_up]
    _moves = cycle(moves)

    val = 1
    pos = 0, 0
    res.append((val, pos))
    times_to_move = 1
    while val < end:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if val >= end:
                    return
                pos = move(pos)
                res.append((val, pos))
                val += 1
        times_to_move += 1


spiral(347991)
print(res)
