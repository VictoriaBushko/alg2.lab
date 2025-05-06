import unittest
from task1 import calculate_max_experience

class TestCareerExperience(unittest.TestCase):
    def test_example_1(self):
        lines = [
            "4",
            "4",
            "3 1",
            "2 1 5",
            "1 3 2 1"
        ]
        result = calculate_max_experience(lines)
        self.assertEqual(result, 12)

    def test_example_2(self):
        lines = [
            "1",
            "9999"
        ]
        result = calculate_max_experience(lines)
        self.assertEqual(result, 9999)

    def test_custom_case(self):
        lines = [
            "5",
            "6",
            "4 2",
            "5 3 8",
            "2 9 6 1",
            "4 1 7 3 2"
        ]
        result = calculate_max_experience(lines)
        self.assertEqual(result, 31)

    def test_all_zeros(self):
        lines = [
            "3",
            "0",
            "0 0",
            "0 0 0"
        ]
        result = calculate_max_experience(lines)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
