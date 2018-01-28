from src.engine.entity import Entity


class EntityManager:

    def __init__(self):
        """

        """
        self._entities = {}

    def create_entity(self, entity_id):
        """

        :param entity_id: the identifier for the entity to be created
        :type entity_id: string
        """
        entity = Entity.create(entity_id)
        self._entities[entity_id] = entity

    def destroy_entity(self, entity_id):
        """

        :param entity_id:
        :type entity_id: string
        """
        if not self.has_entity(entity_id):
            raise Exception('Entity id ' + entity_id + ' does not exit')
        del self._entities[entity_id]

    def has_entity(self, entity_id):
        """

        :param entity_id:
        :type entity_id: string
        :return:
        :rtype: bool
        """
        return entity_id in self._entities

    def get_entity(self, entity_id):
        """

        :param entity_id:
        :type entity_id: string
        :return:
        :rtype: Entity
        """
        if not self.has_entity(entity_id):
            raise Exception('Entity id ' + entity_id + ' does not exit')
        return self._entities[entity_id]

    def attach_component_to_entity(self, entity_id, component_type, component):
        """

        :param entity_id:
        :type entity_id: string
        :param component_type:
        :type component_type: string
        :param component:
        :type component: Component
        """
        entity = self.get_entity(entity_id)
        entity.attach_component(component_type, component)

    def detach_component_from_entity(self, entity_id, component_type):
        """

        :param entity_id:
        :type entity_id: string
        :param component_type:
        :type component_type: string
        """
        entity = self.get_entity(entity_id)
        entity.detach_component(component_type)

    @staticmethod
    def create():
        """

        :return:
        :rtype: EntityManager
        """
        return EntityManager()
