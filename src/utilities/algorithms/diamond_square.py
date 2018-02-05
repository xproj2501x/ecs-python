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
        self._step(power)

    def _get_cell(self, x_position, y_position):
        return self._map[x_position + (y_position * self._size)]

    def _set_cell(self, x_position, y_position, value):
        position = x_position + (y_position * self._size)
        self._map[position] = self._map[position] if self._map[position] else value

    def _step(self, iterations):
        counter = 1
        while counter < iterations:
            length = math.floor(iterations / counter)
            segments = length
            while segments < self._side:
                # self._square_step()
                segments += length
            counter += 1
        # while length > 2:
        #     self._square_step([0, 0], length)
        #     self._diamond_step([0, 0], math.floor(length / 2))
        #     # length = math.floor(length / 2)

    def _square_step(self, top_left, length):
        if top_left[0] + length > self._size - 1 or top_left[1] + length > self._size - 1:
            return
        center = [top_left[0] + math.floor(length / 2), top_left[1] + math.floor(length / 2)]
        if (center[0] >= self._size) or (center[1] >= self._size):
            return
        top_right = [top_left[0] + length, top_left[1]]
        bottom_left = [top_left[0], top_left[1] + length]
        bottom_right = [top_left[0] + length, top_left[1] + length]
        height = self._calculate_height([
            top_left,
            top_right,
            bottom_left,
            bottom_right
        ])
        self._set_cell(center[0], center[1], height)
        if (top_right[0] + length) < self._size:
            self._square_step(top_right, length)
        if (bottom_left[1] + length) < self._size:
            self._square_step(bottom_left, length)
    
    def _diamond_step(self, left, length):
        center = [(left[0] + length), left[1]]
        if (center[0] >= self._size) or (center[1] >= self._size):
            return
        print(left[1])
        print('center x {0} y {1}'.format(center[0], center[1]))
        top = [left[0] + length, left[1] - length]
        bottom = [left[0] + length, left[1] + length]
        right = [left[0] + (2 * length), left[1]]
        height = self._calculate_height([
            left,
            top,
            right,
            bottom])
        self._set_cell(center[0], center[1], height)
        if (left[0] + (2 * length)) < self._size:
            self._diamond_step([left[0] + (2 * length), left[1]], length)
        if (left[1] + (2 * length)) < self._size:
            self._diamond_step()
        # if(left[1] + (2 * length)) < self._size:
        #     self._diamond_step([left[0], left[1] + (2 * length)], length)
            # self._diamond_step([left[0] - length, left[1] + length], length)
            # self._diamond_step([left[0] + length, left[1] + length], length)
        # if (right[0] + length) < self._size:
        #     self._diamond_step([right[0], right[1]], length)

    def _square(self, start, length):
        pass

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
