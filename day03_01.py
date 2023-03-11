import string

# read file
with open('day03.txt', 'r') as f:
    data = f.read().splitlines()


# get all lower and upper case letters
letters = string.ascii_letters

count = 0
for i in data:
    comaprtment_1 = i[:len(i)//2]
    comaprtment_2 = i[len(i)//2:]

    for j in comaprtment_1:
        if j in comaprtment_2:
            count += letters.index(j)+1
            break

print(count)
