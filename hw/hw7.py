import random

def random_char(s):
    # return random.choice(s)
    return s[random.randint(0, len(s) - 1)]

print(random_char('ok'))
