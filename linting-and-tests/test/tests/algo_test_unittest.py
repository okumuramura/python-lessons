import unittest

from app.algorithm import longest_ones


class TestAlgo(unittest.TestCase):
    def test_longest_ones_zero_ones(self):
        data = '000000000'
        res = longest_ones(data)
        self.assertEqual(res, 0)

    def test_longest_ones_all_ones(self):
        data = '11111'
        res = longest_ones(data)
        self.assertEqual(res, 5)


# py -m pip install pytest
