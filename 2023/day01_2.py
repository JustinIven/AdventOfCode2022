# read file
with open('2023/day01.txt', 'r') as f:
    data = f.read().splitlines()

digit_map = {
    "nine": "9",
    "eight": "8",
    "seven": "7",
    "six": "6",
    "five": "5",
    "four": "4",
    "three": "3",
    "two": "2",
    "one": "1"
}

res = 0
for i in data:
    for key, value in digit_map.items():
        i = i.replace(key, value)

    digits = "".join(j for j in i if j.isdigit())
    res += int(digits[0] + digits[-1])

print(res)
