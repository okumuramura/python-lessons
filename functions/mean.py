def my_max(a0, *args):
    m = a0
    for e in args:
        if e > m:
            m = e

    return m


#  print(my_max())  ->  Exception...
print(my_max(2))  # 2
print(my_max(5, 7, 2, 1, 9, 3))  # 9
