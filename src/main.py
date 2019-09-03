import pygame
from src.game import Game


def main():
    pygame.init()
    pygame.display.set_caption("Test game 1")
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.flip()

    game = Game(
        screen=screen,
        speed=5,
        x=50,
        y=50,
        w=50,
        h=75,
    )

    clock = pygame.time.Clock()
    while True:
        clock.tick(100)
        if game.tick():
            break

    pygame.quit()
