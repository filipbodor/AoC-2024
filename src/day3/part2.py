f = open('../../inputs/day3.txt', 'r').read().strip()
counter = 0

class State:
    DO = 1
    DONT = 2

def getState(x, state):
    a = x[::-1].find(')(od')
    b = x[::-1].find(")(t'nod")

    if state == State.DO:
        if (a == -1 and b != -1) or (b < a and b != -1):
            return State.DONT
        return State.DO
    if (a != -1 and b == -1) or (a < b and a != -1):
        return State.DO
    return State.DONT

def mul(x):
    a = x.split(')')
    if len(a) > 1:
        b = a[0].split(',')
        if len(b) == 2:
            try:
                print(int(b[0]), int(b[1]))
                return int(b[0]) * int(b[1])
            except:
                return 0
    return 0

def mul_(x):
    a = x.split(')')
    if len(a) > 1:
        b = a[0].split(',')
        if len(b) == 2:
            try:
                print('dis', int(b[0]), int(b[1]))
                return int(b[0]) * int(b[1])
            except:
                return 0
    return 0

f = f.split('mul(')
state = getState(f[0], State.DO)
for i in range(1, len(f)):
    if state == State.DO:
        counter += mul(f[i])
    else:
        mul_(f[i])
    
    state = getState(f[i], state)

print(counter)
