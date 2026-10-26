import pygame

from settings import WIDTH, HEIGHT
from game import Game
from assets import load_sprites

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    font  = pygame.font.SysFont("arial", 28, bold=True)

    clock = pygame.time.Clock()

    sprites = load_sprites()

    game = Game(screen, font, sprites, clock)
    game.run()

main()