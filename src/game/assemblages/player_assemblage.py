from src.engine.assemblage import Assemblage


class PlayerAssemblage(Assemblage):

    @property
    def position(self):
        return self._get_component('POSITION')

    def __init__(self, entity):
        Assemblage.__init__(self, entity)

    def _get_component(self, component_type):
        return self._entity.get_component[component_type]
