f = open('../../inputs/day3.txt', 'r').read().strip()
counter = 0

def mul(x):
    a = x.split(')')
    if len(a) > 1:
        b = a[0].split(',')
        if len(b) == 2:
            try:
                return int(b[0]) * int(b[1])
            except:
                return 0
    return 0

f = f.split('mul(')
for i in range(1, len(f)):
    counter += mul(f[i])

print(counter)