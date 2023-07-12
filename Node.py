class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.father = None

    def insert(self, node):
        self.children.append(node)
        node.father = self

    def remove(self):
        if self.father:
            self.father.children.remove(self)
            self.father = None
