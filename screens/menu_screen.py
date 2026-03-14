"""Main menu screen with title, buttons, and click feedback text."""

from constants import BG_DARK_COLOR, GOLD_COLOR, WHITE_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH
from ui.button import Button
from ui.label import Label
from ui.panel import Panel


class MenuScreen:
    """Build and control the menu UI."""

    def __init__(self) -> None:
        panel_width = 400
        panel_height = 460
        panel_x = (WINDOW_WIDTH - panel_width) // 2
        panel_y = (WINDOW_HEIGHT - panel_height) // 2
        center_x = WINDOW_WIDTH // 2
        button_x = center_x - 130

        # Labels
        game_title = Label(center_x, panel_y + 60, "AlgoRace", color=GOLD_COLOR, font_size=48, centered=True)
        game_subtitle = Label(center_x, panel_y + 125, "Race Against the Algorithm", color=WHITE_COLOR, font_size=16, centered=True)
        game_tagline = Label(center_x, panel_y + 148, "Built with Python + Pygame", color=WHITE_COLOR, font_size=16, centered=True)

        # Buttons
        start_button = Button(button_x, panel_y + 210, 260, 55, "START")
        history_button = Button(button_x, panel_y + 280, 260, 55, "HISTORY")
        exit_button = Button(button_x, panel_y + 350, 260, 55, "EXIT")

        # Empty feedback until user clicks any button.
        self._feedback_label = Label(center_x, panel_y + 430, "", color=WHITE_COLOR, font_size=16, centered=True)

        # Main container panel
        menu_panel = Panel(panel_x, panel_y, panel_width, panel_height)
        menu_panel.add(game_title)
        menu_panel.add(game_subtitle)
        menu_panel.add(game_tagline)
        menu_panel.add(start_button)
        menu_panel.add(history_button)
        menu_panel.add(exit_button)
        menu_panel.add(self._feedback_label)

        self._panel = menu_panel

    def handle_event(self, event) -> str | None:
        """Handle a click and return the next state if needed."""
        result = self._panel.handle_event(event)
        if result == "START":
            self._feedback_label.update_text("You clicked START")
            return "EDITOR"
        if result == "HISTORY":
            self._feedback_label.update_text("You clicked HISTORY")
            return "HISTORY"
        if result == "EXIT":
            self._feedback_label.update_text("You clicked EXIT")
            return "QUIT"

        return None

    def update(self, mouse_pos) -> None:
        """Update hover states based on current mouse position."""
        self._panel.update(mouse_pos)

    def draw(self, screen) -> None:
        """Draw menu background and all panel children."""
        screen.fill(BG_DARK_COLOR)
        self._panel.draw(screen)