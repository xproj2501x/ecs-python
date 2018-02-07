import math


class DiamondSquare:

    def __init__(self):
        self._size = None
        self._side = None
        self._map = None
        self._min_value = None
        self._max_value = None

    def build(self, power, min_value, max_value):
        self._size = (2 ** power) + 1
        self._side = self._size - 1
        self._min_value = min_value
        self._max_value = max_value
        self._map = [None] * (self._size * self._size)
        self._set_cell(0, 0, self._min_value)
        self._set_cell(self._size - 1, 0, self._min_value)
        self._set_cell(0, self._size - 1, self._min_value)
        self._set_cell(self._size - 1, self._size - 1, self._min_value)
        self._step(self._side)
        return self._map

    def _get_cell(self, x_position, y_position):
        return self._map[x_position + (y_position * self._size)]

    def _set_cell(self, x_position, y_position, value):
        position = x_position + (y_position * self._size)
        self._map[position] = self._map[position] if self._map[position] else value

    def _step(self, size):
        half = math.floor(size / 2)
        if half < 1:
            return
        for y in range(half, self._side, size):
            for x in range(half, self._side, size):
                self._square_step(x, y, half)
        for y in range(0, self._side + 1, half):
            for x in range((y + half) % size, self._side + 1, size):
                self._diamond_step(x, y, half)
        self._step(math.floor(size / 2))

    def _square_step(self, x, y, length):
        height = self._calculate_height([
            [x - length, y - length],
            [x + length, y + length],
            [x - length, y + length],
            [x + length, y - length]
        ])
        self._set_cell(x, y, height)

    def _diamond_step(self, x, y, length):
        height = self._calculate_height([
            [x, y - length],
            [x, y + length],
            [x - length, y],
            [x + length, y]
        ])
        self._set_cell(x, y, height)

    def _calculate_height(self, corners):
        sum = 0
        count = 0
        for corner in corners:
            if corner[0] >= 0 and corner[1] >= 0:
                if corner[0] < self._size and corner[1] < self._size:
                    sum += self._get_cell(corner[0], corner[1])
                    count += 1
        return 1

    def _reset(self):
        pass
