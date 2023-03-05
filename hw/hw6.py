import random
import logging

logging.basicConfig(level=logging.INFO)

def random_digit_sum():
    n = random.randint(100, 999)
    logging.info('generated: %d', n)
    s = 0
    while n != 0:
        s += n % 10
        n //= 10

    return s

print(random_digit_sum())
