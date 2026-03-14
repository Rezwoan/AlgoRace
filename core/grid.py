import pygame
from constants import (
    GRID_ROWS, GRID_COLS, CELL_SIZE, GRID_OFFSET_X, GRID_OFFSET_Y,
    EMPTY, WALL, START, END,
    COLOR_CELL_EMPTY, COLOR_CELL_WALL, COLOR_CELL_START, COLOR_CELL_END,
    COLOR_GRID_LINE
)

# Map each logical cell state to a display color.
CELL_COLORS = {
    EMPTY : COLOR_CELL_EMPTY,
    WALL  : COLOR_CELL_WALL,
    START : COLOR_CELL_START,
    END   : COLOR_CELL_END,
}

# Grid class.
class Grid:
    # Initialize grid data.
    def __init__(self):
        self._rows = GRID_ROWS
        self._cols = GRID_COLS
        self._cells = []
        for _ in range(self._rows):
            row_cells = []
            for _ in range(self._cols):
                row_cells.append(EMPTY)
            self._cells.append(row_cells)

    # Get cell value.
    def get_cell(self, row, col):
        return self._cells[row][col]

    # Set cell value.
    def set_cell(self, row, col, value):
        self._cells[row][col] = value

    # Reset all cells.
    def reset(self):
        for row in range(self._rows):
            for col in range(self._cols):
                self._cells[row][col] = EMPTY

    # Count wall cells.
    def count_walls(self):
        return sum(
            1 for row in self._cells for cell in row if cell == WALL
        )

    # Check cell bounds.
    def is_in_bounds(self, row, col):
        return 0 <= row < self._rows and 0 <= col < self._cols

    # Convert mouse px to cell.
    def mouse_to_cell(self, mx, my):
        col = (mx - GRID_OFFSET_X) // CELL_SIZE
        row = (my - GRID_OFFSET_Y) // CELL_SIZE
        if self.is_in_bounds(row, col):
            return (row, col)
        return None

    # Convert cell to top-left px.
    def cell_to_pixel(self, row, col):
        px = GRID_OFFSET_X + col * CELL_SIZE
        py = GRID_OFFSET_Y + row * CELL_SIZE
        return (px, py)

    # Draw full grid.
    def draw(self, screen):
        for row in range(self._rows):
            for col in range(self._cols):
                cell_value = self._cells[row][col]
                color = CELL_COLORS[cell_value]
                px, py = self.cell_to_pixel(row, col)
                pygame.draw.rect(screen, color, (px, py, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, COLOR_GRID_LINE, (px, py, CELL_SIZE, CELL_SIZE), 1)