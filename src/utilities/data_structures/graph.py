from src.utilities.data_structures.vertex import Vertex


class Graph:

    def __init__(self):
        self._vertices = {}

    def __len__(self):
        return len(self._vertices)

    def __contains__(self, key):
        if self.get_vertex(key, self._root):
            return True
        return False
    
    def add_vertex(self, key, data):
        if self._has_vertex(key):
            raise Exception('Vertex id {0} already exists in the graph'.format(key))
        vertex = Vertex(key, data)
        self._vertices[key] = vertex

    def get_vertex(self, key):
        if not self._has_vertex(key):
            raise Exception('Vertex id {0} does not exist in the graph'.format(key))
        return self._vertices[key]

    def remove_vertex(self, key):
        if not self._has_vertex(key):
            raise Exception('Vertex id {0} does not exist in the graph'.format(key))
        vertex = self._vertices[key]
        del self._vertices[key]

    def add_edge(self, vertex1_key, vertex2_key, weight):
        """

        :param vertex1_key:
        :type vertex1_key:
        :param vertex2_key:
        :type vertex2_key:
        :param weight:
        :type weight:

        :return:
        :rtype:
        """
        if not self._has_vertex(vertex2_key):
            raise Exception('Vertex id {0} does not exist in the graph'.format(vertex2_key))
        vertex = self.get_vertex(vertex1_key)
        vertex.add_edge(vertex2_key, weight)

    def remove_edge(self, vertex1_key, vertex2_key):
        vertex = self.get_vertex(vertex1_key)
        vertex.remove_edge(vertex2_key)

    def _has_vertex(self, key):
        return key in self._vertices

    def _has_edge(self, vertex1_key, vertex2_key):
        """

        :param vertex1_key:
        :param vertex2_key:

        :return:
        :rtype: bool
        """
        vertex = self.get_vertex(vertex1_key)
        return vertex.has_edge(vertex2_key)

    @staticmethod
    def create():
        return Graph()
