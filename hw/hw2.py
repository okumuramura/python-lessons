def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False

print(is_leap_year(2023))
print(is_leap_year(2012))
