"""Reusable text label component."""

import pygame
from constants import FONT_NAME, WHITE_COLOR


class Label:
    """Display-only text element with optional centered alignment."""

    def __init__(self, x: int, y: int, text: str, color=WHITE_COLOR, font_size: int = 22, centered: bool = False):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font_size = font_size
        self.centered = centered

    def update(self, mouse_pos) -> None:
        """No-op update to match common UI component interface."""
        _ = mouse_pos

    def handle_event(self, event) -> None:
        """No-op event handler because labels are not interactive."""
        _ = event
        return None

    def update_text(self, new_text: str) -> None:
        """Change the current label text."""
        self.text = new_text

    def draw(self, screen) -> None:
        """Render text at top-left or centered position."""
        font = pygame.font.SysFont(FONT_NAME, self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rectangle = text_surface.get_rect()

        if self.centered:
            text_rectangle.center = (self.x, self.y)
        else:
            text_rectangle.topleft = (self.x, self.y)

        screen.blit(text_surface, text_rectangle)