class DiamondSquare:

    def __init__(self):
        self._size = None
        self._map = None

    def build(self, power):
        self._size = (2 ** power) + 1
        self._map = [None] * (2 ** self._size)

    def _get_cell(self, x_position, y_position):
        return self._map[x_position + (y_position * self._size)]

    def _set_cell(self, x_position, y_position, value):
        position = x_position + (y_position * self._size)
        self._map[position] = self._map[position] if self._map[position] else value

    def _diamond_step(self, point, side):
        pass

    def _square_step(self, point, side):
        length = side
        if side <= 2:
            return
        while length < self._size:
            self._set_cell(point[0] + side, point[1] + side, 1)
            length += side
        self._diamond_step(point, side / 2)

    def _reset(self):
        pass
