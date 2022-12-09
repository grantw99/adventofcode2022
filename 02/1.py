# COL 1: A for rock, B for paper, C for scissors (opponent)
# COL 2: X for rock, Y for paper, Z for scissors (your move to win)
# Scoring:
#   Point for shape:
#       Rock: 1
#       Paper: 2
#       Scissors: 3
#   Point for outcome:
#       Lose: 0
#       Draw: 3
#       Win: 6

points = []

point_table = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

with open('input.txt') as infile:
    for row in infile:
        r = row.replace("\n", '')
        print(f'{r}: points ({point_table[r]})')
        points.append(point_table[r])

print(sum(points))
