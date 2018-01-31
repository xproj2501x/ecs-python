import pygame
from pygame.locals import *

from src.services.log_service import LogService
from src.engine.entity_manager import EntityManager
from src.engine.component_manager import ComponentManager
from src.engine.assemblage_manager import AssemblageManager
from src.engine.system_manager import SystemManager
from src.engine.state_manager import StateManager
from src.engine.event_manager import EventManager


MILLISECONDS = 1000
FRAME_RATE = 60
FRAME_DURATION = MILLISECONDS / FRAME_RATE
MAX_FRAME_SKIP = 5


class Engine:

    def __init__(self, managers):
        # self._log_service = LogService.create()
        self._running = False
        self._currentTick = 0
        self._lastTick = 0
        self._delta = 0
        self._pygame = pygame
        self._entity_manager = managers['entity_manager']
        self._component_manager = managers['component_manager']
        self._assemblage_manager = managers['assemblage_manager']
        # self._state_manager = managers['state_manager']

    def stop(self):
        self._running = False

    def main(self):
        while self._running:
            for event in self._pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    # self._state_manager.run(event.key)
                    pass
            self._tick()
            self._pygame.display.flip()



    def _tick(self):
        timestamp = self._pygame.time.get_ticks()
        if timestamp <= self._lastTick + FRAME_DURATION:
            delta = timestamp - self._lastTick
            self._update(delta)
            self._render(delta)
            self._lastTick = timestamp

    def start(self):
        self._running = True
        self._pygame.init()
        screen = self._pygame.display.set_mode((640, 480))
        self._pygame.display.set_caption('ECS Python')
        background = self._pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        clock = self._pygame.time.Clock()
        self._lastTick = self._pygame.time.get_ticks()
        self.main()

    def _update(self, delta):
        pass

    def _render(self, delta):
        self._pygame.display.flip()

    @staticmethod
    def create(config):
        entity_manager = EntityManager.create()
        component_manager = ComponentManager.create(config.COMPONENT_TEMPLATES)
        assemblage_manager = AssemblageManager.create({
            'entity_manager': entity_manager,
            'component_manager': component_manager,
            'templates': config.ASSEMBLAGE_TEMPLATES
        })
        # state_manager = StateManager.create(config.STATE)
        managers = {
            'entity_manager': entity_manager,
            'component_manager': component_manager,
            'assemblage_manager': assemblage_manager,
            'system_manager': SystemManager.create(),
            # 'state_manager': StateManager.create(),
            'event_manager': EventManager.create()
        }
        return Engine(managers)
