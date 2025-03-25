import unittest
from Task_1 import TreeNode, sum_of_depths

class TestSumOfDepths(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(sum_of_depths(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test_small_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(sum_of_depths(root), 6)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(sum_of_depths(root), 6)

    def test_large_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        self.assertEqual(sum_of_depths(root), 13)

if __name__ == "__main__":
    unittest.main()
