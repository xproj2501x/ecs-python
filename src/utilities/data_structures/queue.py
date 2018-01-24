class Queue:

    @property
    def length(self):
        """

        :return:
        :rtype: int
        """
        return len(self._data)

    def __init__(self):
        """

        """
        self._data = []

    def enqueue(self, element):
        """

        :param element:
        :type element:
        """
        self._data.append(element)

    def dequeue(self):
        """

        """
        if self.length:
            return self._data.pop(0)

    def peek(self):
        """

        """
        if self.length:
            return self._data[0]
        else:
            return 0

    def clear(self):
        """

        """
        self._data = []
