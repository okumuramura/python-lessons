def digits_sum(n):
    if n == 0:
        return 0
    return digits_sum(n // 10) + n % 10


print(digits_sum(11037))
