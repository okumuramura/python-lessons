def pyramid(n):
    for i in range(1, n*2, 2):
        print(' ' * ((n*2 - i) // 2) + '*' * i + ' ' * ((n*2 - i) // 2))

pyramid(10)
