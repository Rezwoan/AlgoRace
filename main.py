# main.py
import pygame
from game import Game

# Main entry method.
def main() -> None:
    # Run game loop.
    pygame.init()
    game = Game()

    try:
        game.run()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()