"""Reusable clickable button component."""

import pygame
from constants import COLOR_BTN, COLOR_BTN_HOVER, COLOR_BTN_TEXT, FONT_NAME


class Button:
    """Simple rectangular button with hover and click behavior."""

    def __init__(self, x: int, y: int, width: int, height: int, text: str, font_size: int = 22):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.hovered = False

    def update(self, mouse_pos) -> None:
        """Track whether the mouse is currently over the button."""
        self.hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event) -> str | None:
        """Return the button label when left-clicked while hovered."""
        if self.is_clicked(event):
            return self.text
        return None

    def draw(self, screen) -> None:
        """Render button background, border, and centered text."""
        color = COLOR_BTN_HOVER if self.hovered else COLOR_BTN
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, COLOR_BTN_TEXT, self.rect, width=1, border_radius=8)

        font = pygame.font.SysFont(FONT_NAME, self.font_size)
        text_surface = font.render(self.text, True, COLOR_BTN_TEXT)
        text_rectangle = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rectangle)

    def is_clicked(self, event) -> bool:
        """Check if current event is a valid left-click on this button."""
        return (
            self.hovered
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        )