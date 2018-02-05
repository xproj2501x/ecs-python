from src.utilities.data_structures.binary_node import BinaryNode


class BinaryTree:

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, key):
        if self.get_node(key, self._root):
            return True
        return False

    def insert_node(self, data, key):
        new_node = BinaryNode(data, key)
        if not self._root:
            self._root = new_node
        else:
            self._insert_node(self._root, new_node)
        self._size += 1

    def get_node(self, key, current_node=None):
        current_node = current_node if current_node else self._root
        if key == current_node.key:
            return current_node.data
        elif key < current_node.key:
            return self.get_node(key, current_node.left_child)
        else:
            return self.get_node(key, current_node.right_child)

    def remove_node(self, key, split_tree=False):
        if self._size > 1:
            node = self.get_node(key, self._root)
            if node:
                node.remove()
                self._size -= 1
            if split_tree:
                return node
        elif self._size == 1 and self._root.key == key:
            return BinaryTree.create()
        else:
            raise Exception('Key {0} not found in tree'.format(key))

    def _insert_node(self, current_node, new_node):
        if new_node.key < current_node.key:
            if current_node.left_child:
                current_node.left_child = new_node
            else:
                self._insert_node(current_node.left_child, new_node)
        else:
            if current_node.right_child:
                self._insert_node(current_node.right_child, new_node)
            else:
                current_node.right_child = new_node

    @staticmethod
    def create(root=None):
        """
        Static factory method
        :param root:
        :return: BinaryNode

        :return:
        :rtype: BinaryTree
        """
        binary_tree = BinaryTree()
        if root:
            binary_tree.insert_node(root, root.key)
        return binary_tree
