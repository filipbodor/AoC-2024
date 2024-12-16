f = [i for i in open('../../inputs/day6.txt', 'r').read().strip().split('\n')]
axeId = 0
obstaclesY = {}
obstaclesX = {}
visited = set()

for i in range(len(f)):
    for j in range(len(f[0])):
        if f[i][j] == '^':
            position = (j, i)
            visited.add(position)

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

while True:
    if axeId == 0:
        closest = findClosest(position[1], obstaclesX[position[0]], False)

        if closest != abs(float("inf")):
            visited.update({(position[0], i) for i in range(position[1] - 1, closest, -1)})
            position = (position[0], closest + 1)
        else:
            visited.update({(position[0], i) for i in range(position[1] - 1, -1, -1)})
            break
    
    elif axeId == 1:
        closest = findClosest(position[0], obstaclesY[position[1]], True)

        if closest != abs(float("inf")):
            visited.update({(i, position[1]) for i in range(position[0] + 1, closest)})
            position = (closest - 1, position[1])
        else:
            visited.update({(i, position[1]) for i in range(position[0] + 1, len(f[0]))})
            break
    
    elif axeId == 2:
        closest = findClosest(position[1], obstaclesX[position[0]], True)

        if closest != abs(float("inf")):
            visited.update({(position[0], i) for i in range(position[1] + 1, closest)})
            position = (position[0], closest - 1)
        else:
            visited.update({(position[0], i) for i in range(position[1] + 1, len(f))})
            break
    
    elif axeId == 3:
        closest = findClosest(position[0], obstaclesY[position[1]], False)

        if closest != abs(float("inf")):
            visited.update({(i, position[1]) for i in range(position[0] - 1, closest, -1)})
            position = (closest + 1, position[1])
        else:
            visited.update({(i, position[1]) for i in range(position[0] - 1, -1, -1)})
            break
    
    
    axeId = (axeId + 1) % 4

print(len(visited))