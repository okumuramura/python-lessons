def is_prime(n):
    for a in range(2, int(n ** 0.5)):
        if n % a == 0:
            return False
    
    return True

if __name__ == '__main__':
    n = int(input())
    print(is_prime(n))

    # print(is_prime(7))    # True
    # print(is_prime(2))    # True
    # print(is_prime(162))  # False
