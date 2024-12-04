f = [i for i in open('../../inputs/day4.txt', 'r').read().strip().split('\n')]

axes = [[(1, 1), (-1, -1)], [(-1, 1), (1, -1)]]
ascii_gap = ord('S') - ord('M')
width = len(f[0])
height = len(f)
counter = 0

def find_x_mas(x, y):
    return abs(ord(f[y - 1][x - 1]) - ord(f[y + 1][x + 1])) == ascii_gap and abs(ord(f[y + 1][x - 1]) - ord(f[y - 1][x + 1])) == ascii_gap


for i in range(1, height - 1):
    for j in range(1, width - 1):
        if f[i][j] == 'A':
            counter += find_x_mas(j, i)

print(counter)