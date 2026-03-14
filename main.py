"""Program entrypoint for AlgoRace."""

import pygame

from game import Game


def main() -> None:
    """Initialize pygame, run the game loop, and close cleanly."""
    pygame.init()
    game = Game()

    try:
        game.run()
    finally:
        # Always release pygame resources, even if runtime errors happen.
        pygame.quit()


if __name__ == "__main__":
    main()