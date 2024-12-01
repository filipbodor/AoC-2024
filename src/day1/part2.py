f = [[int(j) for j in i.split()] for i in open('../../inputs/day1.txt', 'r').read().strip().split('\n')]
a, b = [i[0] for i in f], [i[1] for i in f]
memory = {}

result = 0
for left in a:
    if left in memory:
        result += left * memory[left]
    else:
        c = b.count(left)
        memory[left] = c
        result += left * c

print(result)