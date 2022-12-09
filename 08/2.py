import numpy as np

class Tree:
    def __init__(self, height:int):
        self.height = height
        self.scenic_score = 0

rows = []

with open('input.txt') as infile:
	for row in infile:
		r = row.replace('\n', '')
		rows.append([Tree(int(x)) for x in r])

def set_scenic_score(tree_index:int, row:list):
    row_copy_l = [t for t in row[:tree_index]]
    row_copy_r = [t for t in row[tree_index+1:]]
    row_copy_l = reversed([t.height for t in row_copy_l])
    row_copy_r = [t.height for t in row_copy_r]
    l_score = 0
    r_score = 0
    for height in row_copy_l:
        if height < row[tree_index].height:
            l_score += 1
        else:
            l_score += 1
            break
    for height in row_copy_r:
        if height < row[tree_index].height:
            r_score += 1
        else:
            r_score += 1
            break
    if row[tree_index].scenic_score == 0:
        row[tree_index].scenic_score = r_score * l_score
    else:
        row[tree_index].scenic_score = row[tree_index].scenic_score * r_score * l_score

def set_visible(row:list):
	for tree in row:
		tree.set_is_visible(True)

for row in rows:
    for tree_index in range(len(row)):
        set_scenic_score(tree_index, row)

rows = np.array(rows).T.tolist()

for row in rows:
    for tree_index in range(len(row)):
        set_scenic_score(tree_index, row)

scenic_scores = [t.scenic_score for t in np.array(rows).flatten().tolist()]

print(max(scenic_scores))