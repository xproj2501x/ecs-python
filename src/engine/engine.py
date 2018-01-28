from src.engine.entity_manager import EntityManager
from src.engine.component_manager import ComponentManager
from src.engine.assemblage_manager import AssemblageManager
from src.engine.system_manager import SystemManager
from src.engine.state_manager import StateManager
from src.engine.


MILLISECONDS = 1000
FRAME_RATE = 60
FRAME_DURATION = MILLISECONDS / FRAME_RATE
MAX_FRAME_SKIP = 5


class Engine:

    def __init__(self):
        self._running = False
        self._currentTick = 0
        self._lastTick = 0
        self._delta = 0

    def stop(self):
        self._running = False

    def tick(self, timestamp):
        if timestamp < self._lastTick + FRAME_DURATION:
            return
        delta = timestamp - self._lastTick
        self._lastTick = timestamp
        self._update(delta)
        self._render(delta)

    def _start(self, timestamp):
        self._running = True
        self._(timestamp)

    def _update(self, delta):
        pass

    def _render(self, delta):
        pass

    @staticmethod
    def create():
        return Engine()
