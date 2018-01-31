class Component:

    @property
    def entity_id(self):
        """

        :return:
        :rtype:
        """
        return self._entity_id

    @property
    def state(self):
        """

        :return:
        :rtype:
        """
        return self._state

    def __init__(self, entity_id, state):
        """

        :param entity_id:
        :type entity_id: string
        :param state:
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
        :return:
        :rtype: Component
        """
        return Component(id, state)
