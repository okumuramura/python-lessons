def reverse(n):
    nums = []
    while n != 0:
        a = n % 10  # последняя цифра
        nums.append(a)
        n = n // 10
    
    result = 0
    p = 1
    for num in nums[::-1]:
        result += num * p
        p *= 10

    return result

def simple_reverse(n):
    return int(str(n)[::-1])

print(reverse(123456))
print(simple_reverse(123456))
