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
calories_sum = []
for i in calories:
    calories_sum.append(sum(i))


print(sum(sorted(calories_sum)[-3:]))