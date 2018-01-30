class DiamondSquare:

    def __init__(self):
        self._size = None
        self._map = None

    def build(self, power):
        self._size = (2 ** power) + 1
        self._map = [None] * self._size
        for idx in self._map:
            self._map[idx] = [None] * self._size

    def _get_cell(self, x_position, y_position):
        pass

    def _set_cell(self, x_position, y_position, value):
        pass

    def _diamond_step(self):
        pass

    def _square_step(self):
        pass

    def _reset(self):
        pass
