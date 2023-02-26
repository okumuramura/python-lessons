# file = open('text.txt', 'r')

# for line in file:
#     print(line.rstrip('\n'), end='...\n')

import random

with open('numfiles.txt', 'w') as file:
    file.write(f'{random.randint(-1000, 1000)}\n')
