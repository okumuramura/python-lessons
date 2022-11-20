'''
Вывести negative для отрицательного числа, positive для положительного и zero для нуля

'''

n = int(input())

if n > 0:
    print('positive')
elif n == 0:
    print('zero')
else:
    print('negative')
