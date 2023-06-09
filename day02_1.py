# read file
with open('day02.txt', 'r') as f:
    data = f.read().splitlines()


score = 0
outcomes = {
    'A': {
        'X': 1+3,
        'Y': 2+6,
        'Z': 3+0,
    },
    'B': {
        'X': 1+0,
        'Y': 2+3,
        'Z': 3+6,
    },
    'C': {
        'X': 1+6,
        'Y': 2+0,
        'Z': 3+3,
    }     
}

for i in data:
    moves = i.split(' ')
    score += outcomes[moves[0]][moves[1]]

print(score)