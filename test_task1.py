import unittest
from task1 import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(boyer_moore_search("ababcabcababc", "abc"), [2, 5, 10])

    def test_no_occurrence(self):
        self.assertEqual(boyer_moore_search("abcdefg", "hij"), [])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("abcdefg", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "abc"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(boyer_moore_search("abc", "abcdef"), [])

    def test_multiple_overlapping(self):
        self.assertEqual(boyer_moore_search("aaaaa", "aa"), [0, 1, 2, 3])

    def test_full_match(self):
        self.assertEqual(boyer_moore_search("abc", "abc"), [0])

if __name__ == '__main__':
    unittest.main()
