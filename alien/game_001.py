import sys
import pygame


def run_game():
    # initialize game and create a dispaly object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # set backgroud color
    bg_color = (230, 230, 230)

    # game loop
    while True:
        # supervise keyboard and mouse item
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # fill color
        screen.fill(bg_color)
        # visualiaze the window
        pygame.display.flip()


run_game()
