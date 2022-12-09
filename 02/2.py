points = []

point_table = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1
}

with open('input.txt') as infile:
    for row in infile:
        r = row.replace("\n", '')
        print(f'{r}: points ({point_table[r]})')
        points.append(point_table[r])

print(sum(points))
