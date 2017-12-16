from io import StringIO


def process(stream):
    garbage = False
    block = 0
    score = 0
    count = 0

    while True:
        ch = stream.read(1)
        if ch == '\n' or ch == '':
            break

        if ch == '!':
            stream.read(1)
            continue

        if ch == '<' and not garbage:
            garbage = True
            continue

        if garbage:
            if ch == '>':
                garbage = False
            else:
                count += 1

            continue

        if ch == '{':
            block += 1
            continue

        if ch == '}':
            score += block
            block -= 1
            continue

    if block != 0:
        print(block)
        raise Exception('help!')
    return count


print('test 1')
test_1 = process(StringIO('<>'))
if test_1 != 0:
    print(test_1)
    raise Exception('Test 1')

print('test 2')
test_2 = process(StringIO('<random characters>'))
if test_2 != 17:
    print(test_2)
    raise Exception('Test 2')

print('test 3')
test_3 = process(StringIO('<<<<>'))
if test_3 != 3:
    print(test_3)
    raise Exception('Test 3')

print('test 4')
test_4 = process(StringIO("<{!>}>"))
if test_4 != 2:
    print(test_4)
    raise Exception('Test 4')

print('test 7')
if process(StringIO('<!!>')) != 0:
    raise Exception('Test 7')

print('test 5')
test_5 = process(StringIO('<!!!>>'))
if test_5 != 0:
    print(test_5)
    raise Exception('Test 5')

print('test 6')
if process(StringIO('<{o"i!a,<{i<a>')) != 10:
    raise Exception('Test 6')

with open('day9.txt', 'r') as f:
    print(process(f))
