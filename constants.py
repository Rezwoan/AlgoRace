# constants.py
# Window settings
WINDOW_TITLE = "AlgoRace"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
FPS = 60

# Font settings
FONT_NAME = "consolas"

# Global colors
BG_DARK_COLOR = (18, 18, 30)
WHITE_COLOR = (255, 255, 255)
GOLD_COLOR = (255, 200, 50)

COLOR_BTN = (39, 174, 96)
COLOR_BTN_HOVER = (46,  204, 113)
COLOR_BTN_TEXT = WHITE_COLOR
COLOR_PANEL_BG = (30, 30, 45)

# Grid cell states
EMPTY = 0
WALL = 1
START = 2
END = 3

# Grid layout
GRID_ROWS = 20
GRID_COLS = 30
CELL_SIZE = 30
GRID_OFFSET_X = 20  # Pixels from left edge where the grid starts.
GRID_OFFSET_Y = 60  # Pixels from top edge (extra room for header labels).

# Grid-specific colors
COLOR_CELL_EMPTY = (30, 30, 50)
COLOR_CELL_WALL = (80, 80, 110)
COLOR_CELL_START = (0, 200, 120)
COLOR_CELL_END = (220, 50, 50)
COLOR_GRID_LINE = (50, 50, 75)