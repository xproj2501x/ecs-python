from enum import Enum
from src.game.components.position_component import PositionComponent


class COMPONENTS:
    POSITION = 'POSITION'


COMPONENT_TEMPLATES = {
    'POSITION': PositionComponent
}

# POSITION = {
#     'X_COORDINATE': 'int',
#     'Y_COORDINATE': 'int',
#     'Z_COORDINATE': 'int'
# }
# TRANSFORM = {
#     'ROTATE': 'int',
#     'X_SCALE': 'int',
#     'Y_SCALE': 'int'
# }
# TWEEN = {
#     'X_START': 'int',
#     'Y_START': 'int',
#     'X_END': 'int',
#     'Y_END': 'int',
#     'SPEED': 'int',
#     'CURRENT_FRAME': 'int'
# }
# SPRITE = {
#     'SHEET': 'string',
#     'HEIGHT': 'int',
#     'WIDTH': 'int',
#     'X_COORDINATE': 'int',
#     'Y_COORDINATE': 'int',
# }
# ANIMATION = {
#     'NAME': 'string',
#     'SPEED': 'int',
#     'LENGTH': 'int',
#     'CURRENT_FRAME': 'int',
#     'REPEAT': 'bool'
# }
