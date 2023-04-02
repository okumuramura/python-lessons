import os
import random
from app.algorithm import longest_ones

print(f'Hello, {os.getlogin()}\nThis is my app!')
print('app by okumuramura')
string = ''.join(
    [str(random.randint(0, 1)) for _ in range(random.randint(10, 20))]
)
print('string:', string)
print('answer:', longest_ones(string))

# py -m pip install black
# black ./ -l 80 -S
