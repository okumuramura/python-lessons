l = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

l.append(a)
l.extend(l[:len(l)//2])
l.pop()
l.pop(b)
l.insert(c, d)
l.append(l.index(a))

print(*l)
