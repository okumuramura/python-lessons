text = input().lower()
counter = {}
total = 0

for e in text:
    if e != ' ':
        counter[e] = counter.get(e, 0) + 1
        total = total + 1

for key, value in counter.items():
    print(key, value, value / total * 100)
