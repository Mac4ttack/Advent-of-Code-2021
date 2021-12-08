from decimal import ExtendedContext
import statistics as st

CrabLoc = [int(x) for x in open('Advent of Code Day 7 Challenge.txt', "r").readline().split(',',)]

## part 1
med = st.median(CrabLoc)
FuelUsed = sum([abs(med-x) for x in CrabLoc])

print('Fuel Used = ', FuelUsed)
## part 2


Most = max(CrabLoc)
Least = min(CrabLoc)
MinFuel = None

for pos in range(Least, Most):
    FuelCalc = 0
    for crab in CrabLoc:
        moves = abs(crab - pos)
        FuelCalc += (moves**2 + moves) / 2

    if not MinFuel:
        MinFuel = FuelCalc
    elif FuelCalc < MinFuel:
        MinFuel = FuelCalc

print(MinFuel)





