import pygame
import sys


class AlienInavasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while true:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInavasion()
    ai.run_game()

