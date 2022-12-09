

rows = []

with open('input.txt') as infile:
	for row in infile:
		rows.append(row.replace('\n', ''))

