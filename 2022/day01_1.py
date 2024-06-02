# read file
with open('day01.txt', 'r') as f:
    data = f.read().splitlines()


# Split the data into a list of numbers
calories  = [[]]
for i in data:
    if i == "":
        calories  += [[]]
    else:
        calories [-1].append(int(i))


# get biggest sum
biggest_sum = 0
for i in calories:
    biggest_sum = max(biggest_sum, sum(i))


print(biggest_sum)