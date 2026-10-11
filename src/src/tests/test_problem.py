import unittest

from src.problem import solve_knapsack


class TestKnapsack(unittest.TestCase):

    def test_known_optimum(self):
        result = solve_knapsack(
            weights=[3, 4, 2],
            values=[4, 5, 3],
            capacity=7,
        )

        self.assertEqual(result["total_value"], 9)
        self.assertEqual(result["total_weight"], 7)
        self.assertEqual(result["selection"], [1, 1, 0])

    def test_capacity_zero(self):
        result = solve_knapsack([2, 3], [5, 7], 0)

        self.assertEqual(result["total_value"], 0)
        self.assertEqual(result["total_weight"], 0)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            solve_knapsack([1, 2], [5], 3)

    def test_capacity_not_exceeded(self):
        result = solve_knapsack([5, 4, 2], [10, 7, 3], 6)

        self.assertLessEqual(result["total_weight"], 6)


if __name__ == "__main__":
    unittest.main()
