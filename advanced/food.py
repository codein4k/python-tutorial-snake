import random

from settings import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        while True:
            pos = (
                        random.randint(0, GRID_WIDTH  - 1),
                        random.randint(0, GRID_HEIGHT - 1),
                    )

            if pos not in snake_body:
                    return pos

    def draw(self, screen, sprites):
        x, y = self.position
        screen.blit(
            sprites["food"],
            (x * CELL_SIZE, y * CELL_SIZE)
        )

    def respawn(self, snake_body):
        self.position = self.random_position(snake_body)