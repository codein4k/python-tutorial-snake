# simple snake game
# learn Python basics while controlling a snake,
# eating food and growing longer!

import random
import os

# ========== GAME CONFIG ==========
WIDTH = 30
HEIGHT = 15

# directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# ========== HELPERS =======

def clear():
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')

    os.system('cls' if os.name == 'nt' else 'clear')

def draw(snake, food, score):

    clear()

    # grid = []

    # for _ in range(HEIGHT):
    #     row = []
    #     for _ in range(WIDTH):
    #         row.append(' ')
    #     grid.append(row)

    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # walls
    for x in range(WIDTH):
        grid[0][x] = '#'
        grid[HEIGHT - 1][x] = '#'

    for x in range(HEIGHT):
        grid[x][0] = '#'
        grid[x][WIDTH - 1] = '#'

    # food
    # fx = food[0]
    # fy = food[1]
    fx, fy = food
    grid[fy][fx] = '*'

    # snake
    for i,(x,y) in enumerate(snake):
        if i == 0:
            grid[y][x] = '@'
        else:
            grid[y][x] = 'o'

    # render
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

    print(f"Score: {score}")
    print("Move with WASD then press Enter (q for quit)")

# ========== FOOD ==========
def create_food(snake):
    while True:
        food = (
                random.randint(1, WIDTH - 2),
                random.randint(1, HEIGHT - 2)
            )
        
        if food not in snake:
                return food

# ========== GAME ==========

def game():

    snake = [(WIDTH // 2, HEIGHT // 2),
            (WIDTH // 2 - 1, HEIGHT // 2),
            (WIDTH // 2 - 2, HEIGHT // 2)]

    food = create_food(snake)
    direction = RIGHT
    score = 0

    while True:
        draw(snake, food, score)

        key = input("Direction: ")

        if key == 'w' and direction != DOWN:
            direction = UP
        elif key == 's' and direction != UP:
            direction = DOWN
        elif key == 'a' and direction != RIGHT:
            direction = LEFT
        elif key == 'd' and direction != LEFT:
            direction = RIGHT
        elif key == 'q':
            break

        # head = snake[0]
        # head_x = head[0]
        # head_y = head[1]
        head_x, head_y = snake[0]

        # dx = direction[0]
        # dy = direction[1]
        dx, dy = direction

        new_head = (head_x + dx, head_y + dy)

        # WALL COLLISION
        if (new_head[0] == 0 or new_head[0] == WIDTH - 1):
            break

        if(new_head[1] == 0 or new_head[1] == HEIGHT - 1):
            break

        # SELF COLLISION
        if new_head in snake:
            break

        snake.insert(0, new_head)

        # food
        if new_head == food:
            # score = score + 10
            score += 10
            food = create_food(snake)
        else:
            snake.pop()

    # ========== GAME OVER ==========
    print("\n" + "#" * 35)
    print("           GAME OVER")
    print(f"         Final Score: {score}")
    print("#" * 35)

game()