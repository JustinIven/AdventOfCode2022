# read file
with open('2023/day01.txt', 'r') as f:
    data = f.read().splitlines()

res = 0
for i in data:
    digits = "".join(j for j in i if j.isdigit())
    res += int(digits[0] + digits[-1])

print(res)
