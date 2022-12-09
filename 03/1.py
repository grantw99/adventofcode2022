priorities = 0

def get_incorrect_item(left:str, right:str):
    for c in left:
        if c in right:
            if c == c.upper():
                return ord(c) - 38
            return ord(c) - 96
    for c in right:
        if c in left:
            if c == c.upper():
                return ord(c) - 38
            return ord(c) - 96

with open('input.txt') as infile:
    for row in infile:
        rucksack = row.replace('\n', '')
        first_comp = rucksack[:len(rucksack)//2]
        second_comp = rucksack[len(rucksack)//2:]
        priorities += get_incorrect_item(first_comp, second_comp)

print(priorities)