class Assemblage:

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._entity.id

    def __init__(self, name, entity):
        self._name = name
        self._entity = entity

    def _get_component(self, component_type):
        return self._entity.get_component(component_type)
