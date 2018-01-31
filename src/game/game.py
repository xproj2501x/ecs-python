from src.game.components.components import *
from src.game.assemblages.assemblages import *
from src.game.states.states import *


STATES = {}
EVENTS = {
    'NONE': 0x00,
    'START': 0x01,
    'PAUSE': 0x02,
    'STEP': 0x03,
    'STOP': 0x04
}


class GAME:
    COMPONENTS = COMPONENTS
    COMPONENT_TEMPLATES = COMPONENT_TEMPLATES
    ASSEMBLAGES = ASSEMBLAGES
    ASSEMBLAGE_TEMPLATES = ASSEMBLAGE_TEMPLATES
    STATES = STATES
