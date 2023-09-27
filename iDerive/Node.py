class Node(object):
    """Base expression tree node class"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addLeft(self, data):
        self.left = Node(data)

    def addRight(self, data):
        self.right = Node(data)

    def print(self):
        print(self.data)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()


if __name__ == '__main__':
    n1 = Node(1)
    n1.addLeft(2)
    n1.addRight(3)

    n1.print()
