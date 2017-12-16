from io import StringIO


def process(stream):
    garbage = False
    block = 0
    score = 0

    while True:
        ch = stream.read(1)
        if ch == '\n' or ch == '':
            break

        if ch == '!':
            stream.read(1)
            continue

        if ch == '<':
            garbage = True
            continue

        if garbage:
            if ch == '>':
                garbage = False

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
    return score


print('test 1')
test_1 = process(StringIO('{}\n'))
if test_1 != 1:
    print(test_1)
    raise Exception('Test 1')

print('test 2')
if process(StringIO('{{{}}}')) != 6:
    raise Exception('Test 2')

print('test 3')
if process(StringIO('{{},{}}')) != 5:
    raise Exception('Test 3')

print('test 8')
test_8 = process(StringIO("{{{},{},{{}}}}"))
if test_8 != 16:
    print(test_8)
    raise Exception('Test 8')

print('test 4')
test_4 = process(StringIO("{<a>,<a>,<a>,<a>}"))
if test_4 != 1:
    print(test_4)
    raise Exception('Test 4')

print('test 5')
test_5 = process(StringIO('{{<ab>},{<ab>},{<ab>},{<ab>}}'))
if test_5 != 9:
    print(test_5)
    raise Exception('Test 5')

print('test 6')
if process(StringIO('{{<!!>},{<!!>},{<!!>},{<!!>}}')) != 9:
    raise Exception('Test 6')

print('test 7')
if process(StringIO('{{<a!>},{<a!>},{<a!>},{<ab>}}')) != 3:
    raise Exception('Test 7')

with open('day9.txt', 'r') as f:
    print(process(f))
