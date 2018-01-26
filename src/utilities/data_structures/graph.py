from src.utilities.data_structures.vertex import Vertex


class Graph:

    def __init__(self):
        self._vertices = {}

    def add_vertex(self, vertex_id, data):
        if self._has_vertex(vertex_id):
            raise Exception('Vertex id {0} already exists in the graph'.format(vertex_id))
        vertex = Vertex(vertex_id, data)
        self._vertices[vertex_id] = vertex

    def get_vertex(self, vertex_id):
        if not self._has_vertex(vertex_id):
            raise Exception('Vertex id {0} does not exist in the graph'.format(vertex_id))
        return self._vertices[vertex_id]

    def remove_vertex(self, vertex_id):
        if not self._has_vertex(vertex_id):
            raise Exception('Vertex id {0} does not exist in the graph'.format(vertex_id))

    def add_edge(self, vertex1_id, vertex2_id):
        pass

    def remove_edge(self, vertex1_id, vertex2_id):
        pass

    def _has_vertex(self, vertex_id):
        return vertex_id in self._vertices

    def _has_edge(self, vertex1_id, vertex2_id):
        pass

    @staticmethod
    def create():
        return Graph()
