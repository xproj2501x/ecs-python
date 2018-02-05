from src.utilities.algorithms.diamond_square import DiamondSquare


class WorldGenerator:

    def __init__(self):
        self._size = None
        self._diamond_square = DiamondSquare()

    def build(self):
        self._diamond_square.build(4, 1, 255)

    def _generate_height_map(self):
        pass
