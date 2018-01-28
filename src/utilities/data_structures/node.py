class Node:

    @property
    def data(self):
        return self._data

    def __init__(self, data):
        self._data = data
