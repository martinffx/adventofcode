with open('day5.2.txt', 'r') as f:
    line = f.read()
    maze = line.splitlines()

# maze = [0, 3, 0, 1, -3]

index = 0
count = 0
while index < len(maze):
    x = int(maze[index])
    if x >= 3:
        maze[index] = x - 1
    else:
        maze[index] = x + 1
    index += x
    count += 1

print(maze)
print(count)
