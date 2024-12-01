f = [[int(j) for j in i.split()] for i in open('../../inputs/day1.txt', 'r').read().strip().split('\n')]
a, b = [i[0] for i in f], [i[1] for i in f]

a.sort()
b.sort()

result = 0
for i in range(len(f)):
    result += abs(a[i] - b[i])

print(result)