'''
Вводится два числа. Вывести наибольшее из них.

3 7
7
'''

a, b = map(int, input().split())

if a > b:
    print(a)
else:
    print(b)
