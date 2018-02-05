VERSION = '0.1'

try:
    import sys
    # import random
    # import math
    # import os
    # import getopt
    # import pygame
    # from socket import *
    # from pygame.locals import *
    #
    # from src.engine.engine import Engine
    # from src.engine.state_manager import StateManager
    # from src.engine.entity_manager import EntityManager
    #
    # from src.game.game import GAME
    # from src.game.states.loading_state import LoadingState
    # from src.game.states.playing_state import PlayingState
    from src.game.generators.world_generator import WorldGenerator
    from src.utilities.data_structures.binary_tree import BinaryTree
    from src.utilities.algorithms.diamond_square import DiamondSquare
except ImportError as err:
    print("couldn't load module. {0}".format(err))
    sys.exit(2)


# def load_png(name):
#     """
#     Load image file and return image object
#     :param name:
#     :return:
#     """
#     fullname = os.path.join('data', name)
#     try:
#         image = pygame.image.load(fullname)
#         if image.get.alpha() is None:
#             image = image.convert()
#         else:
#             image = image.convert_alpha()
#     except pygame.error as err:
#         print("Cannot load image: {0}".format(fullname))
#         raise SystemExit(err)
#     return image, image.get_rect()


# STATES = {
#     'LOADING': LoadingState(),
#     'PLAYING': PlayingState()
# }


def main():
    world_generator = WorldGenerator()
    world_generator.build()
    # pygame.init()
    # screen = pygame.display.set_mode((640, 480))
    # entity_manager = EntityManager.create()
    # engine = Engine.create(GAME)
    # engine.start()
    # state_manager = StateManager.create(screen, STATES, 'LOADING')
    #
    # pygame.display.set_caption('ECS Python')
    #
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    # background.fill((0, 0, 0))
    #
    # basic_font = pygame.font.SysFont(None, 48)
    #
    # screen.blit(background, (0, 0))
    # pygame.display.flip()
    #
    # clock = pygame.time.Clock()
    # while 1:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             return
    #         elif event.type == pygame.KEYDOWN:
    #             state_manager.run(event.key)
    #
    #     engine.tick(pygame.time.get_ticks())
    #     state_manager.render(basic_font)
    #     pygame.display.flip()


if __name__ == '__main__':
    main()
