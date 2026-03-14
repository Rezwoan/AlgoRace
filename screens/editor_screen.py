# editor_screen.py
import pygame
from constants import BG_DARK_COLOR, WHITE_COLOR, GOLD_COLOR, FONT_NAME
from core.grid import Grid
from ui.label import Label

# Editor screen class.
class EditorScreen:
    # Initialize editor UI.
    def __init__(self):
        self._grid = Grid()
        editor_title = Label(20, 15, "MAZE EDITOR", color=WHITE_COLOR, font_size=22)
        wall_count = Label(20, 45, "Walls: 0", color=WHITE_COLOR, font_size=16)
        self._wall_count_label = wall_count
        self._labels = [editor_title, wall_count]

    # Handle editor events.
    def handle_event(self, event):
        pass

    # Update editor state.
    def update(self, mouse_pos):
        _ = mouse_pos  # Not used yet.
        self._wall_count_label.update_text(f"Walls: {self._grid.count_walls()}")

    # Draw editor screen.
    def draw(self, screen):
        screen.fill(BG_DARK_COLOR)
        self._grid.draw(screen)
        for label in self._labels:
            label.draw(screen)