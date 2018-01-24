class Component:

    @property
    def entity_id(self):
        return self.entity_id

    @property
    def state(self):
        return self._state

    def __init__(self, entity_id, state):
        if not entity_id:
            raise Exception('Entity id cannot be null')
        if not state:
            raise Exception('Component state cannot be null')
        self.entity_id = entity_id
        self._state = state

    def update(self, state):
        for key in state:
            if not self._state[key]:
                raise Exception('Invalid key ' + key + ' for component')
        for key in state:
            self._state[key] = state[key]

    @staticmethod
    def create(id, state):
        return Component(id, state)
