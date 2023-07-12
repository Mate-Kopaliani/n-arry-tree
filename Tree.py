from Node import *


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def size(self):
        return self.__size(self.root)

    def __size(self, node):
        if node is None:
            return 0
        n = 1
        for i in node.children:
            n += self.__size(i)
        return n

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0
        n = 0
        for child in node.children:
            n = max(n, self.__height(child))

        return n + 1

    def traverse(self):
        self.__traverse(self.root)

    def __traverse(self, node):
        if node is None:
            return
        print(node.value)
        for i in node.children:
            self.__traverse(i)

    def delete(self, target):
        self.__delete_node(self.root, target)

    def __delete_node(self, node, target):
        if node is None:
            return

        if node.value == target:
            node.remove()
            return

        for i in node.children:
            self.__delete_node(i, target)

    def lca(self, node1, node2):
        return self.__lca_helper(self.root, node1, node2)

    def __lca_helper(self, current_node, node1, node2):
        if current_node is None or current_node == node1 or current_node == node2:
            return current_node

        lca_candidates = []
        for child in current_node.children:
            lca = self.__lca_helper(child, node1, node2)
            if lca is not None:
                lca_candidates.append(lca)

        if len(lca_candidates) == 2:
            return current_node
        elif len(lca_candidates) == 1:
            return lca_candidates[0]
        else:
            return None

