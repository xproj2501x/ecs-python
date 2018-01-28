from src.utilities.data_structures.graph import Graph


class Assemblage:


    @property
    def id(self):
        return self._entity.id

    def __init__(self, entity):
        self._entity = entity

    def attach_component(self, component_type, component):
        self._entity.attach_component(component_type, component)
