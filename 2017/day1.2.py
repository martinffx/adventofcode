with open('day1.txt') as f:
    captcha = f.readline()

length = len(captcha) - 1
incr = int(length / 2)


def next_index(index):
    v = index + incr
    if v > length:
        return v - length
    return v


sum = 0
for index in range(0, length):
    index = int(index)
    current = captcha[index]
    next_val = captcha[next_index(index)]

    if current == next_val:
        sum += int(current)

print(sum)
