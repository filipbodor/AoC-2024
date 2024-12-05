rules_raw, updates = (lambda x: [[(lambda z: (int(z[0]), int(z[1])))(i.split('|')) for i in x[0].split('\n')], [[int(j) for j in i.split(',')] for i in x[1].split('\n')]])(open('../../inputs/day5.txt', 'r').read().strip().split('\n\n'))
counter = 0

rules = {}
for rule in rules_raw:
    if rule[0] in rules:
        rules[rule[0]].append(rule[1])
    else:
        rules[rule[0]] = [rule[1]]


def getUpdateValue(update):
    for i in range(len(update)):
        for j in update[:i]:
            if j in rules.get(update[i], []):
                return 0
    return update[len(update) // 2]

for update in updates:
    counter += getUpdateValue(update)

print(counter)