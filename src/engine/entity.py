import uuid


class Entity:

    @property
    def id(self):
        return self._id

    def __init__(self, entity_id):
        if not entity_id:
            raise Exception('Entity id cannot be null')
        self._id = entity_id
        self._components = {}

    def attach_component(self, component_type, component):
        if self.has_component(component_type):
            raise Exception('Component type ' + component_type + ' already attached to entity ' + self._id)
        self._components[type] = component

    def has_component(self, component_type):
        return component_type in self._components

    def get_component(self, component_type):
        if not self.has_component(component_type):
            raise Exception('Component type ' + component_type + ' not attached to entity ' + self._id)
        return self._components[component_type]

    def detach_component(self, component_type):
        if not self.has_component(component_type):
            raise Exception('Component type ' + component_type + ' not attached to entity ' + self._id)
        del self._components[component_type]

    @staticmethod
    def create(entity_id):
        entity_id = entity_id if entity_id else uuid.uuid4()
        return Entity(entity_id)
