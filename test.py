import unittest
from Node import *
from Tree import *


class TreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = Tree(0)
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n4 = Node(4)
        self.n5 = Node(5)
        self.tree.root.insert(self.n1)
        self.tree.root.insert(self.n2)
        self.n1.insert(self.n3)
        self.n1.insert(self.n4)
        self.n2.insert(self.n5)

    def test_size(self):
        self.assertEqual(6,self.tree.size())

    def test_height(self):
        self.assertEqual(3,self.tree.height())

    def test_lca(self):
        lca_node = self.tree.lca(self.n3, self.n5)
        self.assertEqual(0, lca_node.value)

        lca_node = self.tree.lca(self.n4, self.n5)
        self.assertEqual(0, lca_node.value)

        lca_node = self.tree.lca(self.n3, self.n4)
        self.assertEqual(1, lca_node.value)

        lca_node = self.tree.lca(self.n1, self.n2)
        self.assertEqual(0, lca_node.value)

        lca_node = self.tree.lca(self.n3, self.n3)
        self.assertEqual(3, lca_node.value)


if __name__ == '__main__':
    unittest.main()
