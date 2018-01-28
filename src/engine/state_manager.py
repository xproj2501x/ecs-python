class StateManager:

    def __init__(self, screen, states, current_state):
        self._locked = False
        self._screen = screen
        self._states = states
        self._current_state = current_state

    def run(self, input):
        state = self._states[self._current_state]
        self._current_state = state.next(input)

    def render(self, basic_font):
        text = basic_font.render(self._current_state, True, (255, 0, 0), (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.centerx = self._screen.get_rect().centerx
        text_rect.centery = self._screen.get_rect().centery

        self._screen.fill((255, 255, 255))
        self._screen.blit(text, text_rect)


    @staticmethod
    def create(screen, states, current_state):
        return StateManager(screen, states, current_state)
