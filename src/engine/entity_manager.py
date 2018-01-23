from entity import Entity


class EntityManager:

    def __init__(self):
        self._entities = {}

    def create_entity(self, id):
        entity = Entity.create(id)
        self._entities[id] = entity

    def destroy_entity(self, id):
        if not self.has_entity(id):
            raise Exception('Entity id ')
        del self._entities[id]

    def has_entity(self, id):
        return id in self._entities

    def attach_component_to_entity(self):
        pass

    def detach_component_from_entity(self):
        pass

    @staticmethod
    def create():
        return EntityManager()
