from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint
        import pandas as pd
        num1 = randint(0, 100)
        array = [num1]

        res = solution(array)
        self.assertTrue(isinstance(res, pd.Series))
        self.assertEqual(num1, res[0])