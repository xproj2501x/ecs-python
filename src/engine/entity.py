import uuid


class Entity:

    @property
    def id(self):
        """

        :return:
        :rtype: string
        """
        return self._id

    def __init__(self, entity_id):
        """
        :param entity_id: the identifier for the entity
        :type entity_id: string
        """
        if not entity_id:
            raise Exception('Entity id cannot be null')
        self._id = entity_id
        self._components = {}

    def attach_component(self, component_type, component):
        """
        :param component_type: the type of component to be attached
        :type component_type: string
        :param component: the component to be attached
        :type component: Component
        """
        if self.has_component(component_type):
            raise Exception('Component type ' + component_type + ' already attached to entity ' + self._id)
        self._components[type] = component

    def has_component(self, component_type):
        """
        :param component_type: the type of component
        :type component_type: string

        :return:
        :rtype: bool
        """
        return component_type in self._components

    def get_component(self, component_type):
        """
        :param component_type: the type of component
        :type component_type: string

        :return: the component of specified type
        :rtype: Component
        """
        if not self.has_component(component_type):
            raise Exception('Component type ' + component_type + ' not attached to entity ' + self._id)
        return self._components[component_type]

    def detach_component(self, component_type):
        """
        :param component_type: the type of component
        :type component_type: string
        """
        if not self.has_component(component_type):
            raise Exception('Component type ' + component_type + ' not attached to entity ' + self._id)
        del self._components[component_type]

    @staticmethod
    def create(entity_id=None):
        """
        :param entity_id: the id for the entity
        :type entity_id: string

        :return: the created entity
        :rtype: Entity
        """
        entity_id = entity_id if entity_id else uuid.uuid4()
        return Entity(entity_id)
