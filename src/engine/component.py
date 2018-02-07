class Component:

    @property
    def entity_id(self):
        """
        Read only property

        :return: The id of the parent entity
        :rtype: str
        """
        return self._entity_id

    def __init__(self, entity_id, state):
        """
        Constructor
        :param entity_id: The id of the parent entity
        :type entity_id: string
        :param state: The initial state of the component
        :type state: dict
        """
        if not entity_id:
            raise Exception('Entity id cannot be null')
        if not state:
            raise Exception('Component state cannot be null')
        self._entity_id = entity_id
        self._state = state

    def update(self, state):
        """
        Updates the component state with new values
        :param state:
        :type state: dict
        """
        for key in state:
            if not self._state[key]:
                raise Exception('Invalid key ' + key + ' for component')
        for key in state:
            self._state[key] = state[key]

    @staticmethod
    def create(entity_id, state):
        """

        :param entity_id:
        :type entity_id: string
        :param state:
        :type state: dict
        :return: A new component
        :rtype: Component
        """
        return Component(entity_id, state)
