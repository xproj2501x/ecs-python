from src.engine.component import Component


class Keys:
    x_coordinate = 'X_COORDINATE'
    y_coordinate = 'Y_COORDINATE'
    z_coordinate = 'Z_COORDINATE'


class PositionComponent(Component):

    @property
    def x_coordinate(self):
        return self._state[Keys.x_coordinate]

    @property
    def y_coordinate(self):
        return self._state['Y_COORDINATE']

    @property
    def z_coordinate(self):
        return self._state['Z_COORDINATE']

    def __init__(self, entity_id, state):
        Component.__init__(self, entity_id, state)
