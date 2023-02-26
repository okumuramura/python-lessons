counter = {}

with open('text.txt', 'r') as file:
    for line in file:
        for c in line.rstrip('\n').lower():
            if c.isalpha():
                counter[c] = counter.get(c, 0) + 1


print(max(counter.items(), key=lambda x: x[1]))
