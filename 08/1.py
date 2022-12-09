import numpy as np

class Tree:
	def __init__(self, height:int):
		self.height = height
		self.visible = False

	def set_height(self, height:int):
		self.height = height
	
	def set_is_visible(self, visible:bool):
		self.visible = visible
	
	def is_visible(self) -> bool:
		return self.visible

rows = []

with open('input.txt') as infile:
	for row in infile:
		r = row.replace('\n', '')
		rows.append([Tree(int(x)) for x in r])

def set_visibility(tree_index:int, row:list):
	row_copy_l = [t for t in row[:tree_index]]
	row_copy_r = [t for t in row[tree_index+1:]]
	row_copy_l = [t.height for t in row_copy_l]
	row_copy_r = [t.height for t in row_copy_r]
	if max(row_copy_l) < row[tree_index].height or max(row_copy_r) < row[tree_index].height:
		row[tree_index].set_is_visible(True)

def set_visible(row:list):
	for tree in row:
		tree.set_is_visible(True)

for row in rows:
	for tree_index in range(len(row)):
		if 0 < tree_index < 98 and not row[tree_index].visible:
			set_visibility(tree_index, row)
		else:
			row[tree_index].set_is_visible(True)

rows = np.array(rows).T.tolist()

for row in rows:
	for tree_index in range(len(row)):
		if 0 < tree_index < 98 and not row[tree_index].visible:
			set_visibility(tree_index, row)
		else:
			row[tree_index].set_is_visible(True)

visible_trees = 0

for row in rows:
	for tree in row:
		if tree.visible:
			visible_trees += 1

print(visible_trees)