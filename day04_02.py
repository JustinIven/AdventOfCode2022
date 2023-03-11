# read file
with open('day04.txt', 'r') as f:
    data = f.read().splitlines()

section_all = [ [ [ int(k) for k in j.split('-') ] for j in i.split(',') ] for i in data ]

count = 0
for i in section_all:
    if i[0][1] >= i[1][0] and i[0][0] <= i[1][1]:
        count += 1

print(count)