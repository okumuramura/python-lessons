n = int(input())
c0 = 0

for _ in range(n):
    a = int(input())
    if a == 0:
        c0 += 1

print(min(c0, n - c0))
