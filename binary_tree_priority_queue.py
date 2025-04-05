class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.priority > current.priority:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def extract_max(self):
        if self.root is None:
            return None

        parent = None
        current = self.root

        while current.left:
            parent = current
            current = current.left

        if parent is None:
            self.root = self.root.right
        else:
            parent.left = current.right

        return current.value

    def peek(self):
        if self.root is None:
            return None

        current = self.root
        while current.left:
            current = current.left

        return current.value

    def display(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is None:
            return []
        return self._inorder_traversal(node.left) + [(node.value, node.priority)] + self._inorder_traversal(node.right)


if __name__ == "__main__":
    pq = BinaryTreePriorityQueue()
    pq.insert("Task 3", 3)
    pq.insert("Task 5", 5)
    pq.insert("Task 2", 2)
    pq.insert("Task 4", 4)
    pq.insert("Task 6", 1)
    pq.insert("Task 7", 7)


    print("Черга після вставки:", pq.display())
    print("Елемент із найвищим пріоритетом:", pq.peek())
    print("Видалений елемент:", pq.extract_max())
    print("Черга після видалення:", pq.display())
