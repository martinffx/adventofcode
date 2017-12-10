import operator

blocks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
hist = []
length = len(blocks)


def get_index(index):
    val = index + 1
    if val < length:
        return val
    return val - length


while blocks not in hist:
    max_index, max_value = max(enumerate(blocks), key=operator.itemgetter(1))
    hist.append(list(blocks))
    blocks[max_index] = 0
    index = get_index(max_index)
    while max_value > 0:
        blocks[index] += 1
        max_value -= 1
        index = get_index(index)

x = hist.index(blocks)
y = len(hist)

# part 1
print(y)

# part 2
print(y - x)
