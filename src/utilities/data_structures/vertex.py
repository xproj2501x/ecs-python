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

    def add_edge(self, vertex_id, weight):
        if self._has_edge(vertex_id):
            raise Exception('Vertex {0} already connected to vertex {1}'.format(self._id, vertex_id))
        self._edges[vertex_id] = weight

    def remove_edge(self, vertex_id):
        if not self._has_edge(vertex_id):
            raise Exception('Vertex {0} not connected to vertex {1}'.format(self._id, vertex_id))
        del self._edges[vertex_id]

    def _has_edge(self, vertex_id):
        """

        :param vertex_id:
        :type vertex_id: int
        :return:
        :rtype: bool
        """
        return vertex_id in self._edges

    @staticmethod
    def create():
        """
        Static factory method
        :return:
        :rtype: Vertex
        """
        return Vertex()
