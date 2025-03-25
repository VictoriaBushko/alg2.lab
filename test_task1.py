import unittest
from main import is_monotonic



class TestMonotonicArray(unittest.TestCase):
    def test_increasing(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))

    def test_non_monotonic(self):
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4]))

    def test_constant_values(self):
        self.assertTrue(is_monotonic([3, 3, 3, 3]))

    def test_single_element(self):
        self.assertTrue(is_monotonic([10]))

    def test_empty_array(self):
        self.assertTrue(is_monotonic([]))

if __name__ == "__main__":
    unittest.main()
