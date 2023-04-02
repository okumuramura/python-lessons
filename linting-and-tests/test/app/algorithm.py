from typing import List, Union, Optional, Callable


# 10101110101101011
def longest_ones(s):
    ones = 0
    max_ones = 0
    for c in s:
        if c == '1':
            ones += 1
            max_ones = max(max_ones, ones)
        else:
            ones = 0
    return max_ones


# aAbBcCdDeE -> 5
def count_upcase(s: Union[List[str], str]) -> int:
    count = 0
    for c in s:
        if c.isupper():
            count += 1
    return count


def say_hello(name: str, _return: bool) -> Optional[str]:
    s = f'hello, {name}!'
    print(s)
    if _return:
        return s
    return None

# py -m pip install flake8


def cmp(a: int, b: int) -> bool:
    return a > b


def test_cmp(a: int, b: int, cmp: Callable[[int, int], bool]) -> bool:
    return cmp(a, b)
