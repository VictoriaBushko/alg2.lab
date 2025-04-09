import unittest
from main import bfs, find_root_vertex

class TestGraph(unittest.TestCase):

    def test_bfs_true(self):
        graph = {1: [2], 2: [3], 3: [4], 4: [1]}
        self.assertTrue(bfs(1, 4, graph))

    def test_bfs_false(self):
        graph = {1: [2], 2: [], 3: [4], 4: []}
        self.assertFalse(bfs(1, 4, graph))

    def test_find_root_vertex_exists(self):
        graph = {1: [2], 2: [3], 3: [4], 4: [1]}
        self.assertIn(find_root_vertex(4, graph), [1, 2, 3, 4])

    def test_find_root_vertex_not_exists(self):
        graph = {1: [2], 2: [], 3: [4], 4: []}
        self.assertEqual(find_root_vertex(4, graph), -1)

if __name__ == '__main__':
    unittest.main()
