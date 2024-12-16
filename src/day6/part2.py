f = [i for i in open('../../inputs/day6.txt', 'r').read().strip().split('\n')]
obstaclesY = {}
obstaclesX = {}
counter = 0

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '^':
            start = (j, i)

        elif f[i][j] == "#":
            if i in obstaclesY:
                obstaclesY[i].append(j)
            else:
                obstaclesY[i] = [j]

            if j in obstaclesX:
                obstaclesX[j].append(i)
            else:
                obstaclesX[j] = [i]

def findClosest(pos, others, isIncreasing):
    closest = float("inf")
    for i in others:
        if (isIncreasing and i > pos and i - pos < closest) or (not isIncreasing and i < pos and pos - i < closest): 
            closest = i - pos if isIncreasing else pos - i
    return pos + closest if isIncreasing or closest == float("inf") else pos - closest

def isCycle(start, obsX, obsY, obstacle):
    axeId = 0
    position = start
    visited = []

    while True:
        if axeId == 0:
            closest = findClosest(position[1], obsX.get(position[0], []) + ([obstacle[1]] if position[0] == obstacle[0] else []), False)

            if closest != abs(float("inf")):
                position = (position[0], closest + 1)
            else:
                return False
        
        elif axeId == 1:
            closest = findClosest(position[0], obsY.get(position[1], []) + ([obstacle[0]] if position[1] == obstacle[1] else []), True)

            if closest != abs(float("inf")):
                position = (closest - 1, position[1])
            else:
                return False
        
        elif axeId == 2:
            closest = findClosest(position[1], obsX.get(position[0], []) + ([obstacle[1]] if position[0] == obstacle[0] else []), True)

            if closest != abs(float("inf")):
                position = (position[0], closest - 1)
            else:
                return False
        
        elif axeId == 3:
            closest = findClosest(position[0], obsY.get(position[1], [])  + ([obstacle[0]] if position[1] == obstacle[1] else []), False)

            if closest != abs(float("inf")):
                position = (closest + 1, position[1])
            else:
                return False
            
        if [position, axeId] in visited:
            break
        
        visited += [[position, axeId]]
        axeId = (axeId + 1) % 4

    return True

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '.':
            counter += isCycle(start, obstaclesX, obstaclesY, (j, i))

print(counter)