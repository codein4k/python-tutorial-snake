import pygame
import sys

from settings import (
    BG_COLOR, WHITE, HEIGHT, WIDTH,
    UP, DOWN, LEFT, RIGHT
)

from snake import Snake
from food import Food

class Game:
    def __init__(self, screen, font, sprites, clock):
        self.screen = screen
        self.font = font
        self.sprites = sprites
        self.clock = clock
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.game_over = False
        self.speed = 5

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                 if not self.game_over:
                    if   event.key == pygame.K_w: self.snake.set_direction(UP)
                    elif event.key == pygame.K_s: self.snake.set_direction(DOWN)
                    elif event.key == pygame.K_a: self.snake.set_direction(LEFT)
                    elif event.key == pygame.K_d: self.snake.set_direction(RIGHT)
                 else:
                    if event.key == pygame.K_r:
                        self.reset()

    # ===== UI =====
    def draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(170)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            game_over = self.font.render("GAME OVER", True, WHITE)
            restart   = self.font.render("Press R To Restart", True, WHITE)

            self.screen.blit(
                game_over,
                game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
            )
            self.screen.blit(
                restart,
                restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            )

    def draw(self):
        self.screen.fill(BG_COLOR)

        self.food.draw(self.screen, self.sprites)
        self.snake.draw(self.screen, self.sprites)

        self.draw_ui()
        pygame.display.flip()

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        if self.snake.check_collision():
            self.game_over = True
            return

        if self.snake.body[0] == self.food.position:
            self.snake.grow = True
            self.food.respawn(self.snake.body)
            self.score += 1
            self.speed = self.speed + 0.5

    def run(self):
        while True:
            # handle inputs
            self.handle_input()
            # update game status
            self.update()
            # draw game components
            self.draw()
            # delay
            self.clock.tick(self.speed)