with open('day1.txt') as f:
    captcha = f.readline()

length = len(captcha)
sum = 0
prev = None
for index in range(0, length):
    current = captcha[index]
    if not prev:
        prev = captcha[-1]

    if current == prev:
        sum += int(current)

    prev = current

print(sum)
