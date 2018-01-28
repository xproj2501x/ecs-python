from src.engine.state import State


class PlayingState(State):

    def __init__(self):
        State.__init__(self, 'PLAYING')

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def next(self, input):
        if input == 27:
            return 'LOADING'
        return 'PLAYING'