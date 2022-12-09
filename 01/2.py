elves = {0: 0}

starting_elf = 0

with open('input.txt') as infile:
    for row in infile:
        if row == '\n':
            starting_elf += 1
            elves[starting_elf] = 0
        else:
            elves[starting_elf] += int(row)

e = sorted(elves.values())
e.reverse()

print(sum(e[0:3]))