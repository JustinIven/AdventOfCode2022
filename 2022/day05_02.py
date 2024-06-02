# read file
with open('day05.txt', 'r') as f:
	data = f.read()

str_stacks, str_moves = data.split('\n\n')
str_stacks = str_stacks.splitlines()
str_moves = str_moves.splitlines()

# parse stacks
stacks = {}
for i in str_stacks[-2::-1]:
	for j in range(1, len(i), 4):
		if i[j] != ' ':
			if j//4+1 in stacks:
				stacks[j//4+1] += i[j]
			else:
				stacks[j//4+1] = [i[j]]

# parse moves
moves = []
for i in str_moves:
	temp = i.split(' ')
	moves.append([int(temp[1]), int(temp[3]), int(temp[5])])


# move
for i in moves:
	stacks[i[2]] += stacks[i[1]][-i[0]:]
	stacks[i[1]] = stacks[i[1]][:-i[0]]


# print the top of each stack
anwser = ''
for i in range(1, len(stacks)+1):
	anwser += stacks[i][-1]

print(anwser)