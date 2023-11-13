import unittest
from math_quiz import rand_int, rand_operation, do_operation


class TestMathGame(unittest.TestCase):

    def test_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rand_operation(self):
        # Test if the random operator is one of '+', '-', or '*'
        for _ in range(1000):  # Test a large number of random values
            operator = rand_operation()
            self.assertIn(operator, ['+', '-', '*'])

    def test_do_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (10, 2, '+', '10 + 2', 12),
            (7, 4, '-', '7 - 4', 3),
            (3, 5, '*', '3 * 5', 15),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = do_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)



if __name__ == "__main__":
    unittest.main()
