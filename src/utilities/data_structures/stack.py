class Stack:

    @property
    def length(self):
        return len(self._data)
    
    def __init__(self):
        self._data = []

    def push(self, element):
        pass

    def pop(self):
        pass

    def clear(self):
        self._data = []
