priorities = 0

groups = [[]]

def calc_priority(c:str):
    if c == c.upper():
        return ord(c) - 38
    return ord(c) - 96

with open('input.txt') as infile:
    for row in infile:
        rucksack = row.replace('\n', '')
        if len(groups[len(groups) - 1]) == 3:
            groups.append([rucksack])
        else:
            groups[len(groups) - 1].append(rucksack)

for group in groups:
    for c in group[0]:
        if c in group[1] and c in group[2]:
            priorities += calc_priority(c)
            break
print(priorities)