with open('day5.txt', 'r') as f:
    line = f.read()
    maze = line.splitlines()

index = 0
count = 0
while index < len(maze):
    x = int(maze[index])
    maze[index] = x + 1
    index += x
    count += 1

print(count)
