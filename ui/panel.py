# panel.py
import pygame
from constants import COLOR_PANEL_BG

# Panel class.
class Panel:
    # Initialize panel data.
    def __init__(self, x: int, y: int, width: int, height: int, color=COLOR_PANEL_BG):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.children = []

    # Add child element.
    def add(self, element) -> None:
        self.children.append(element)

    # Update child elements.
    def update(self, mouse_pos) -> None:
        for child in self.children:
            child.update(mouse_pos)

    # Forward event to children.
    def handle_event(self, event):
        for child in self.children:
            result = child.handle_event(event)
            if result:
                return result
        return None

    # Draw panel and children.
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        for child in self.children:
            child.draw(screen)