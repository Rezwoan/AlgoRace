# label.py
import pygame
from constants import FONT_NAME, WHITE_COLOR

# Label class.
class Label:
    # Initialize label data.
    def __init__(self, x: int, y: int, text: str, color=WHITE_COLOR, font_size: int = 22, centered: bool = False):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font_size = font_size
        self.centered = centered

    # Update hook.
    def update(self, mouse_pos) -> None:
        _ = mouse_pos
        return None

    # Event hook.
    def handle_event(self, event) -> None:
        _ = event
        return None

    # Change label text.
    def update_text(self, new_text: str) -> None:
        self.text = new_text

    # Draw label text.
    def draw(self, screen) -> None:
        font = pygame.font.SysFont(FONT_NAME, self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rectangle = text_surface.get_rect()

        if self.centered:
            text_rectangle.center = (self.x, self.y)
        else:
            text_rectangle.topleft = (self.x, self.y)

        screen.blit(text_surface, text_rectangle)