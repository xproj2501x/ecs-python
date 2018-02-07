class Queue:

    @property
    def length(self):
        """
        Returns the length of the queue

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
        Adds an element to the end of the queue

        :param element: the element to be added to the queue
        :type element: object
        """
        self._data.append(element)

    def dequeue(self):
        """
        Removes an element from the front of queue and returns it

        :return: the first element in the queue
        :rtype: object
        """
        if self.length:
            return self._data.pop(0)

    def peek(self):
        """
        Returns the first element on the queue if available, otherwise returns false

        :return: the first element in the queue
        :rtype: object
        """
        if self.length:
            return self._data[0]
        else:
            return False

    def clear(self):
        """
        Resets the queue
        """
        self._data = []
