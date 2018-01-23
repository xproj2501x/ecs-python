from entity import Entity


class EntityManager:

    def __init__(self):
        self._entities = {}

    def create_entity(self, entity_id):
        entity = Entity.create(entity_id)
        self._entities[entity_id] = entity

    def destroy_entity(self, entity_id):
        if not self.has_entity(entity_id):
            raise Exception('Entity id ' + entity_id + ' does not exit')
        del self._entities[entity_id]

    def has_entity(self, entity_id):
        return entity_id in self._entities

    def get_entity(self, entity_id):
        if not self.has_entity(entity_id):
            raise Exception('Entity id ' + entity_id + ' does not exit')
        return self._entities[entity_id]

    def attach_component_to_entity(self, entity_id, component_type, component):
        entity = self.get_entity(entity_id)
        entity.attach_component(component_type, component)

    def detach_component_from_entity(self, entity_id, component_type):
        entity = self.get_entity(entity_id)
        entity.detach_component(component_type)

    @staticmethod
    def create():
        return EntityManager()
