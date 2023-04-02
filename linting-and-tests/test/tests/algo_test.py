import pytest

from app.algorithm import longest_ones, count_upcase


def test_longest_ones_only_ones():
    data = '11111'
    res = longest_ones(data)
    assert res == 5


def test_longest_ones_no_ones():
    data = '0000'
    assert longest_ones(data) == 0


def test_longest_ones_with_int():
    data = 1011101
    with pytest.raises(TypeError):
        longest_ones(data)


@pytest.mark.parametrize(
        ['data', 'exp'],
        [
            ['aBcDE', 3],
            ['abc', 0],
            ['', 0]
        ]
)
def test_count_upcase(data, exp):
    assert count_upcase(data) == exp


# py -m pip install pytest-cov
