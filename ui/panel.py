"""Container component that groups UI elements."""

import pygame

from constants import COLOR_PANEL_BG


class Panel:
    """Simple panel that updates, draws, and dispatches events to children."""

    def __init__(self, x: int, y: int, width: int, height: int, color=COLOR_PANEL_BG):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.children = []

    def add(self, element) -> None:
        """Register a new UI element inside this panel."""
        self.children.append(element)

    def update(self, mouse_pos) -> None:
        """Update all child components."""
        for child in self.children:
            child.update(mouse_pos)

    def handle_event(self, event):
        """Send event to children and return first non-empty result."""
        for child in self.children:
            result = child.handle_event(event)
            if result:
                return result
        return None

    def draw(self, screen) -> None:
        """Draw panel background and all children."""
        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        for child in self.children:
            child.draw(screen)