from collections import deque

def read_last(lines, file):
    last = deque([''] * lines)
    for line in file:
        last.pop()
        last.appendleft(line.strip('\n'))

    return list(last)

with open('hw6.py') as file:
    print(*read_last(5, file), sep='\n', end='')
print()
