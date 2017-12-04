def mod_row(row):
    for index in range(0, len(row)):
        curr = int(row[index])
        for v in range(0, len(row)):
            if v == index:
                continue

            val = int(row[v])

            if curr % val == 0:
                return curr / val

    print(row)
    raise Exception('HELP!')


with open('day2.txt', 'r') as f:
    checksum = 0
    for line in f:
        row = line.split('\t')
        checksum += mod_row(row)

    print(checksum)
