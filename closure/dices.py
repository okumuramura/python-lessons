import random

def dice(n):
    def throw():
        return random.randint(1, n)
    
    return throw

d6 = dice(6)

for i in range(3):
    print(d6())
