from __future__ import annotations

class CleaningArea:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
    
    def contains(self, other:CleaningArea) -> bool:
        if self.start <= other.start and self.end >= other.end:
            return True
        return False

def contain_each_other(left:CleaningArea, right:CleaningArea):
    if left.contains(right) or right.contains(left):
        return 1
    return 0

groups = 0

with open('input.txt') as infile:
    for row in infile:
        r = row.replace('\n', '')
        r_left = r.split(',')[0]
        r_l_start = int(r_left.split('-')[0])
        r_l_end = int(r_left.split('-')[1])
        r_right = r.split(',')[1]
        r_r_start = int(r_right.split('-')[0])
        r_r_end = int(r_right.split('-')[1])
        groups += contain_each_other(CleaningArea(r_l_start, r_l_end), CleaningArea(r_r_start, r_r_end))

print(groups)