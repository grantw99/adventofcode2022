

rows = []

with open('input.txt') as infile:
	for row in infile:
		rows.append(row.replace('\n', ''))

b = rows[0]

for x in range(len(b) - 3):
	tcomp = b[x:x+14]
	if len(set(tcomp)) == 14:
		print(x+14)
		break