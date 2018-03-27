lengths = [106, 16, 254, 226, 55, 2, 1, 166, 177, 247, 93, 0, 255, 228, 60, 36]


def reverse_sublist(lst, curr, length):
    for i in range(length // 2):
        x = (curr + i) % len(lst)
        y = (curr + length - 1 - i) % len(lst)
        lst[x], lst[y] = lst[y], lst[x]


def one():
    elements = list(range(256))
    curr = 0
    skip = 0
    for length in lengths:
        reverse_sublist(elements, curr, length)
        curr += length + skip
        skip += 1

    return elements[0] * elements[1]


def two():
    elements = [ord(str(i)) for i in list(range(256))] + [17, 31, 73, 47, 23]
    curr = 0
    skip = 0
    for i in range(64):
        for length in lengths:
            reverse_sublist(elements, curr, length)
            curr += length + skip
            skip += 1

    [input[i:i + 16] for i in range(0, len(input), 16)]


print("A", one())
print("B", two())
