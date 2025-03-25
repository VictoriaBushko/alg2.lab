import unittest
from Task_1 import min_time_to_paint

class TestPainting(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_time_to_paint(5, 10, [15, 10, 5, 10, 15, 20, 20, 15, 20]), 350)
        self.assertEqual(min_time_to_paint(1, 5, [10, 20, 30]), 300)
        self.assertEqual(min_time_to_paint(3, 2, [5, 10, 15, 20]), 40)

if __name__ == "__main__":
    unittest.main()
