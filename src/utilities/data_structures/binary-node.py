from src.utilities.data_structures.node import Node


class BinaryNode(Node):

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    def __init__(self, data):
        Node.__init__(self, data)
        self._left = None
        self._right = None
