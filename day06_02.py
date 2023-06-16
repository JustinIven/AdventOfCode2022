# read file
with open('day06.txt', 'r') as f:
    data = f.read()

distinct_chars = 14
for i in range(distinct_chars, len(data)+1):
    # convert to set so that duplicates are removed
    if len(set(data[i-distinct_chars:i])) == distinct_chars:
        print(i)
        break
