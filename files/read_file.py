# file = open('text.txt', 'r')

# for line in file:
#     print(line.rstrip('\n'), end='...\n')

import random

with open('numfiles.txt', 'w') as file:
    for _ in range(1000):
        file.write(f'{random.randint(-1000, 1000)}\n')

s = 0
with open('numfiles.txt', 'r') as file:
    for line in file:
        s += int(line)


print('sum:', s)
