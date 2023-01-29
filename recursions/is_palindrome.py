def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0].lower() != s[-1].lower():
        return False
    return is_palindrome(s[1:-1])


print(is_palindrome('Abba'))
print(is_palindrome('abcdef'))
