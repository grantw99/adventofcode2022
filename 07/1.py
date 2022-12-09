

commands = []

with open('input.txt') as infile:
	for row in infile:
		if row.startswith('$'):
			commands.append([row.replace('\n', '')])
		else:
			commands[-1].append(row.replace('\n', ''))

files = {}

current_dir = ''

for command in commands:
	if command[0].startswith('$ cd'):
		newdir = command[0].split(' ')[-1]
		if newdir.startswith('/'):
			current_dir = newdir
		elif newdir == '..':
			current_dir = '/'.join(current_dir.split('/')[:-1])
		else:
			current_dir = current_dir + '/' + newdir
	elif command[0].startswith('$ ls'):
		for subcommand in command:
			if not subcommand.startswith('$ ls') and subcommand[0].isdigit():
				if current_dir.startswith('//'):
					files[current_dir[1:] + '/' + subcommand.split(' ')[-1]] = int(subcommand.split(' ')[0])

dir_sizes = {}

for file in files:
	for folder_index in range(len(file.split('/'))):
		folder = '/'.join(file.split('/')[:folder_index])
		if folder in dir_sizes:
			dir_sizes[folder] += files[file]
		else:
			dir_sizes[folder] = files[file]

print(dir_sizes)

good_dirs = 0

for dir in dir_sizes:
	if dir_sizes[dir] <= 100000:
		good_dirs += dir_sizes[dir]

print(good_dirs)

