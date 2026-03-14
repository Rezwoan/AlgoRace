"""Core game loop and screen-state handling."""

import pygame
from constants import FPS, WINDOW_HEIGHT, WINDOW_TITLE, WINDOW_WIDTH
from screens.menu_screen import MenuScreen


class Game:
    """Owns pygame resources and controls the active screen."""

    def __init__(self) -> None:
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()
        self._running = False
        self._state = "MENU"

        pygame.display.set_caption(WINDOW_TITLE)

        self._menu_screen = MenuScreen()
        self._menu_state = "MENU"
        self._editor_state = "EDITOR"
        self._history_state = "HISTORY"

    def _handle_events(self) -> None:
        """Process input and pass events to the current screen."""
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if self._state == self._menu_state:
                result = self._menu_screen.handle_event(event)
                if result == "QUIT":
                    self._running = False
                elif result:
                    # Keep this placeholder behavior for now since other screens
                    # are not fully implemented yet.
                    if result in (self._editor_state, self._history_state):
                        pass

        if self._state == self._menu_state:
            self._menu_screen.update(mouse_pos)

    def _draw(self) -> None:
        """Render the active screen once per frame."""
        if self._state == self._menu_state:
            self._menu_screen.draw(self._screen)

        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop until the user exits."""
        self._running = True
        while self._running:
            self._handle_events()
            self._draw()
            self._clock.tick(FPS)