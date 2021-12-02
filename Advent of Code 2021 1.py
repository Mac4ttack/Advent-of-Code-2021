with open('Advent of Code Day 1 Challenge.txt', "r") as defile:
    lines = [int(i) for i in defile.readlines()]
    
bourbon,whiskey = 0,0

for i in range(1,len(lines)):
        bourbon += lines[i] > lines[i-1]
        whiskey += i > 2 and sum(lines[i-3:i]) > sum(lines[i-4:i-1])


print(bourbon)
print(whiskey)

defile.close()