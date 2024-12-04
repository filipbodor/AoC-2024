f = [i for i in open('../../inputs/day4.txt', 'r').read().strip().split('\n')]

axes = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
xmas = 'XMAS'
width = len(f[0])
height = len(f)
counter = 0

def find_xmas(x, y):
    c = 0
    for p, q in axes:
        for i in range(4):
            if not (0 <= x + (p * i) < width and 0 <= y + (q * i) < height and f[y + (q * i)][x + (p * i)] == xmas[i]):
                break
        else:
            c += 1
    return c



for i in range(height):
    for j in range(width):
        if f[i][j] == 'X':
            counter += find_xmas(j, i)

print(counter)