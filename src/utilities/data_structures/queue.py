class Queue:

    @property
    def length(self):
        """

        :return: the length of the queue
        :rtype: int
        """
        return len(self._data)

    def __init__(self):
        """

        """
        self._data = []

    def enqueue(self, element):
        """
        Adds an element to the back of the queue
        :param element: the element to be added to the queue
        :type object:
        """
        self._data.append(element)

    def dequeue(self):
        """

        :return: the first element in the queue
        :rtype: object
        """
        if self.length:
            return self._data.pop(0)

    def peek(self):
        """
        :return: the first element in the queue
        :rtype: object
        """
        if self.length:
            return self._data[0]
        else:
            return 0

    def clear(self):
        """

        """
        self._data = []
