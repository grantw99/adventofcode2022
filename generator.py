from os import mkdir

days = []

for day in range(5, 26):
    if len(str(day)) == 1:
        days.append(f'0{day}')
    else:
        days.append(str(day))

for day in days:
    mkdir(day)
    with open(f'{day}/input.txt', 'w') as outfile0,  open(f'{day}/1.py', 'w') as outfile1, open(f'{day}/2.py', 'w') as outfile2:
        outfile1.write("""\n\nrows = []\n\nwith open('input.txt') as infile:\n\tfor row in infile:\n\t\trows.append(row.replace('\\n', ''))\n\n""")
