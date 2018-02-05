from src.utilities.data_structures.node import Node


class BinaryNode(Node):

    @property
    def key(self):
        return self._key

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, node):
        node.parent = self
        self._left_child = node

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, node):
        node.parent = self
        self._right_child = node

    @property
    def parent_node(self):
        return self._parent_node

    @parent_node.setter
    def parent_node(self, parent_node):
        self._parent_node = parent_node

    @property
    def is_root_node(self):
        return self._parent_node is None

    @property
    def is_left_node(self):
        return self._parent_node.left_child == self

    @property
    def is_right_node(self):
        """
        Read only property
        Returns true if the node is a right node of the parent

        :return:
        :rtype: bool
        """
        return self._parent_node.right_child == self

    def __init__(self, key, data, parent=None):
        Node.__init__(self, data)
        self._key = key
        self._left_child = None
        self._right_child = None
        self._parent_node = parent

    def remove(self):
        if self.is_left_node:
            self._parent_node.left_child = None
        else:
            self._parent_node.right_child = None

    @staticmethod
    def create(data, key=None, parent=None):
        """
        Static factory method
        :param data:
        :type data:
        :param key:
        :type key:
        :param parent:
        :type parent: BinaryNode

        :return:
        :rtype: BinaryNode
        """
        return data if type(data) == BinaryNode else BinaryNode(data, key, parent)
