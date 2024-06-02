import string
import numpy as np

# read file
with open('day03.txt', 'r') as f:
    data = f.read().splitlines()

# get all lower and upper case letters
letters = string.ascii_letters


arr = np.array(data).reshape(len(data)//3, 3)


count = 0
for i in arr:
    for j in i[0]:
        if j in i[1] and j in i[2]:
            count += letters.index(j)+1
            break

print(count)
