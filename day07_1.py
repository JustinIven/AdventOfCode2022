from json import dumps

# read file
with open('day07.txt', 'r') as f:
    data = f.read().splitlines()

# parse data
terminal = []
for i in data:  
    # determine if the line is input or output
    if i[0] == '$':
        arguments = i.split(' ')[1:]
        terminal.append({
            'input': arguments,
            'output': []
        })
    else:
        terminal[-1]['output'] += [i]


def path_get(dictionary, path):
    for item in path:
        dictionary = dictionary[item]
    return dictionary

def path_set(dictionary, path, setItem):
    dictionary = path_get(dictionary, path[:-1])
    dictionary[path[-1]] = setItem

print(terminal)

tree = {}
current_folder = []
for i in terminal:
    # move directory
    if i['input'][0] == 'cd':
        if i['input'][1] == '..':
            current_folder = current_folder[:-1]
        else:
            current_folder.append(i['input'][1])
            path_set(tree, current_folder, {})
    
    # list files
    elif i['input'][0] == 'ls':
        for i in i['output']:
            file = i.split(' ')
            if not file[0] == 'dir':
                path_set(tree, current_folder + [file[1]], int(file[0]))




print(dumps(tree, indent=4))

exit()
_size = 0
def get_dir_size(dictionary):
    global _size
    size = 0
    for i in dictionary:
        if isinstance(dictionary[i], int):
            size += dictionary[i]
        else:
            tmp = get_dir_size(dictionary[i])
            if tmp <= 100000:
                size += tmp
                _size += tmp
    return size


print(get_dir_size(tree))

print(_size)