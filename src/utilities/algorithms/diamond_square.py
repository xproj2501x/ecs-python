import math


class DiamondSquare:

    def __init__(self):
        self._size = None
        self._map = None
        self._min_value = None
        self._max_value = None

    def build(self, power, min_value, max_value):
        self._size = (2 ** power) + 1
        self._min_value = min_value
        self._max_value = max_value
        self._map = [None] * (2 ** self._size)
        self._set_cell(0, 0, self._min_value)
        self._set_cell(0, self._size - 1, self._min_value)
        self._set_cell(self._size - 1, 0, self._min_value)
        self._set_cell(self._size - 1, self._size - 1, self._min_value)
        self._square_step([0, 0], math.floor(self._size / 2))

    def _get_cell(self, x_position, y_position):
        return self._map[x_position + (y_position * self._size)]

    def _set_cell(self, x_position, y_position, value):
        position = x_position + (y_position * self._size)
        self._map[position] = self._map[position] if self._map[position] else value

    def _diamond_step(self, start, side):
        if side <= 2:
            return
        print(start)

    def _square_step(self, start, side):
        if side <= 2:
            return
        length = side
        while length < self._size - 1:
            corners = self._find_corners(start, side)
            value = self._calculate_value(corners)
            new_cell = [start[0] + side, start[1] + side]
            self._set_cell(new_cell[0], new_cell[1], value)
            self._diamond_step(new_cell, side)
            length += side

    def _find_corners(self, start, side, square=True):
        corners = []
        if square:
            corners.append(self._get_cell(start[0], start[1]))
            corners.append(self._get_cell(start[0] + (side * 2), start[1]))
            corners.append(self._get_cell(start[0], start[1] + (side * 2)))
            corners.append(self._get_cell(start[0] + (side * 2), start[1] + (side * 2)))
        else:
            corners.append(self._get_cell(start[0] - side, start[1]))
            corners.append(self._get_cell(start[0] + side, start[1]))
            corners.append(self._get_cell(start[0], start[1] + side))
            corners.append(self._get_cell(start[0], start[1] - side))
        return corners

    def _calculate_value(self, corners):
        value = 0
        for corner in corners:
            value += corner
        return value / len(corners)

    def _reset(self):
        pass
