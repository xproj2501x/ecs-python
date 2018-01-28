from src.engine.state import State


class LoadingState(State):

    def __init__(self):
        State.__init__(self, 'LOADING')

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def next(self, input):
        if input == 13:
            return 'PLAYING'
        return self._name

    def render(self):
        pass