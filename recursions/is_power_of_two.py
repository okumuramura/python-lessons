def is_power_of_two(n):
    if n % 2 == 0:
        return is_power_of_two(n // 2)
    return n == 1


print(is_power_of_two(1024))
