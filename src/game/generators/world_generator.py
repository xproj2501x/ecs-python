from src.utilities.algorithms.diamond_square import DiamondSquare


class WorldGenerator:

    def __init__(self):
        self._size = None
        self._diamond_square = DiamondSquare()
        self._world = None

    def build(self):
        self._world = [None] * (4096 ** 2)
        map = self._diamond_square.build(4, 1, 255)
        print(len(self._world))

    def _generate_height_map(self):
        pass
