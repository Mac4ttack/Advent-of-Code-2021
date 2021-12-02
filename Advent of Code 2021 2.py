with open('Advent of Code Day 2 Challenge.txt', "r") as defile:
    lines = defile.readlines()

totforward, curforward, up, down, trajectory, aim = 0, 0, 0, 0, 0, 0

for i in lines:
    if i.split()[0] == 'down':
        down += int(i.split()[1])
    if i.split()[0] == 'up':
        up += int(i.split()[1])

    aim = down - up

    if i.split()[0] == 'forward':
        totforward += int(i.split()[1])
        curforward = int(i.split()[1])
        trajectory += aim * curforward


print((down-up)*totforward);
print(trajectory*totforward)