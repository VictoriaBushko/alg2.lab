import unittest
from Task1 import kruskal

class TestTask1(unittest.TestCase):
    def test_mst_total_length(self):
        edges = [
            (2000, 'K1', 'K2'),
            (1500, 'K2', 'K3'),
            (1800, 'K3', 'K4'),
            (2200, 'K1', 'K4')
        ]
        nodes = {'K1', 'K2', 'K3', 'K4'}
        result = kruskal(edges, nodes)
        self.assertEqual(result, 5300)

    def test_disconnected_graph(self):
        edges = [
            (1000, 'K1', 'K2'),
            (1000, 'K3', 'K4')
        ]
        nodes = {'K1', 'K2', 'K3', 'K4'}
        result = kruskal(edges, nodes)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
