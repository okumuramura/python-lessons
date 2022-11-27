n = int(input())

n0 = n // 100000
n1 = n // 10000 % 10
...

if n0 + n1 + n2 == n3 + n4 + n5:
    print('lucky')
else:
    print('next time')
