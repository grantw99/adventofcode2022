crates = {
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],
	7: [],
	8: [],
	9: []
}

instructions = []

with open('input.txt') as infile:
	lines = infile.readlines()
	for x in reversed(range(8)):
		for y in range(1, 35, 2):
			if lines[x][y] != ' ':
				crates[y//4 + 1].append(lines[x][y])
	for x in range(10, len(lines)):
		inst = lines[x].replace('\n', '').replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
		instructions.append({'repeat': int(inst[0]), 'origin': int(inst[1]), 'dest': int(inst[2])})

for inst in instructions:
    crates_to_move = inst['repeat'] * -1
    i = crates[inst['origin']][crates_to_move:]
    crates[inst['origin']] = crates[inst['origin']][:crates_to_move]
    for val in i:
        crates[inst['dest']].append(val)

print([v[-1] for v in crates.values()])