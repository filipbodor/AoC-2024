levels = [[int(j) for j in i.split()] for i in open('../../inputs/day2.txt', 'r').read().strip().split('\n')]
counter = 0

for level in levels:
    levelLenght = len(level)
    isIncreasing = level[0] < level[1]

    for i in range(levelLenght - 1):
        if not ((isIncreasing and 1 <= level[i + 1] - level[i] <= 3) or (not isIncreasing and 1 <= level[i] - level[i + 1] <= 3)):
            break
    else:
        counter += 1

print(counter)