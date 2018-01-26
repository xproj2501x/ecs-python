class Vertex:

    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    def __init__(self, vertex_id, data):
        self._id = vertex_id
        self._data = data
        self._edges = {}

    def add_edge(self):
        pass

    def remove_edge(self):
        pass

    @staticmethod
    def create():
        """
        Static factory method
        :return:
        :rtype: Vertex
        """
        return Vertex()
