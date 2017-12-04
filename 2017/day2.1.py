with open('day2.txt', 'r') as f:
    checksum = 0
    for line in f:
        row = line.split('\t')
        print(row)
        first = int(row[0])
        rest = row[1:]
        largest, smallest = first, first
        for val in rest:
            i_val = int(val)
            if i_val > largest:
                largest = i_val

            if i_val < smallest:
                smallest = i_val

        print(largest)
        print(smallest)
        print('=======================')
        checksum += (largest - smallest)

print(checksum)
