from itertools import cycle
from functools import partial

res = {}


def move_right(pos):
    return pos[0] + 1, pos[1]


def move_down(pos):
    return pos[0], pos[1] - 1


def move_left(pos):
    return pos[0] - 1, pos[1]


def move_up(pos):
    return pos[0], pos[1] + 1


def bottom_right(pos):
    return pos[0] + 1, pos[1] - 1


def bottom_left(pos):
    return pos[0] - 1, pos[1] - 1


def top_left(pos):
    return pos[0] - 1, pos[1] + 1


def top_right(pos):
    return pos[0] + 1, pos[1] + 1


def get_val(res, key):
    if key in res:
        return res[key]
    return None


def get_adj(pos, res):
    adj = [
        move_right, bottom_right, move_down, bottom_left, move_left, top_left,
        move_up, top_right
    ]
    keys = [str(move(pos)) for move in adj]

    val = 0
    for key in keys:
        if key in res:
            val += res[key][0]

    return val


def spiral(end):
    moves = [move_right, move_down, move_left, move_up]
    _moves = cycle(moves)

    count = 1
    pos = 0, 0
    res[str(pos)] = (count, pos)
    times_to_move = 1
    val = count
    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if val >= end + 2:
                    return
                pos = move(pos)
                val = get_adj(pos, res)
                res[str(pos)] = (val, pos)
                count += 1
        times_to_move += 1


# 347991
spiral(347991)
print(res)
