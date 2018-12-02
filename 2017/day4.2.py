from collections import Counter


def valid(passphrase):
    counter = Counter(passphrase)
    print(counter)
    for k in counter:
        if counter[k] > 1:
            return False
    return True


def anagram(phrase):
    y = list(phrase.strip())
    y.sort()
    return ''.join(y)


with open('day4.txt', 'r') as f:
    valid_count = 0
    for line in f:
        passphrase = map(anagram, line.split(' '))
        if valid(passphrase):
            valid_count += 1

print(valid_count)
