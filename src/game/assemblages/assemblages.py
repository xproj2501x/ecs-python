from enum import Enum
from src.game.assemblages.player_assemblage import PlayerAssemblage
from src.game.components.components import COMPONENTS


class ASSEMBLAGES(Enum):
    PLAYER = 'PLAYER'


ASSEMBLAGE_TEMPLATES = {
    'PLAYER': {
        'constructor': PlayerAssemblage,
        'components': [
            COMPONENTS.POSITION
        ]
    }
}