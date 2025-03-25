class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode, depth=0) -> int:
    if root is None:
        return 0
    return depth + sum_of_depths(root.left, depth + 1) + sum_of_depths(root.right, depth + 1)

def sum_of_leaf_depths(root: TreeNode, depth=0) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return depth
    return sum_of_leaf_depths(root.left, depth + 1) + sum_of_leaf_depths(root.right, depth + 1)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(13)
    root.right.right = TreeNode(11)
    root.right.left = TreeNode(8)
    root.left.left.left = TreeNode(13)


    print("Sum of depths:", sum_of_depths(root))
    print("Sum of leaf depths:", sum_of_leaf_depths(root))
