def counter(start=0, inc=True):
    value = start + 1
    if inc:
        value -= 2

    def increase():
        nonlocal value
        value += 1
        return value

    def decrease():
        nonlocal value
        value -= 1
        return value
    
    if inc:
        return increase
    return decrease

cnt = counter()
cnt2 = counter(inc=False)

print(cnt(), cnt(), cnt())  # 0 1 2
print(cnt2(), cnt2(), cnt2()) # 0 -1 -2
