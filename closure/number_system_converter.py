def dec2n(k):
    def converter(n):
        result = ''
        while n != 0:
            result += str(n % k)
            n = n // k
        
        return result[::-1]

    return converter

dec2bin = dec2n(2)
dec2oct = dec2n(8)

nums = [10, 22, 100]

for num in nums:
    print(num, dec2bin(num), dec2oct(num))
