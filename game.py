# game.py
import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FPS
from screens.menu_screen import MenuScreen
from screens.editor_screen import EditorScreen

# Game class.
class Game:
    # Initialize game state.
    def __init__(self) -> None:
        self._screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()
        self._running = False
        self._state = "MENU"

        pygame.display.set_caption(WINDOW_TITLE)

        self._menu_screen = MenuScreen()
        self._editor_screen = EditorScreen()

    # Handle all runtime events.
    def _handle_events(self) -> None:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if self._state == "MENU":
                result = self._menu_screen.handle_event(event)
                if result == "QUIT":
                    self._running = False
                elif result:
                    self._state = result

            elif self._state == "EDITOR":
                self._editor_screen.handle_event(event)

        if self._state == "MENU":
            self._menu_screen.update(mouse_pos)
        elif self._state == "EDITOR":
            self._editor_screen.update(mouse_pos)

    # Draw active screen.
    def _draw(self) -> None:
        if self._state == "MENU":
            self._menu_screen.draw(self._screen)
        elif self._state == "EDITOR":
            self._editor_screen.draw(self._screen)

        pygame.display.flip()

    # Start game loop.
    def run(self) -> None:
        self._running = True
        while self._running:
            self._handle_events()
            self._draw()
            self._clock.tick(FPS)