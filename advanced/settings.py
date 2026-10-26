# cells & grid
CELL_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 20
WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE

# colors
BG_COLOR = (25,25,35)
WHITE    = (240, 240, 240)

# ========== DIRECTIONS ==========
UP    = (0, -1)
DOWN  = (0,  1)
LEFT  = (-1, 0)
RIGHT = (1,  0)

OPPOSITE = {
    UP:    DOWN,
    DOWN:  UP,
    LEFT:  RIGHT,
    RIGHT: LEFT,
}

# ========== TURN SPRITES ==========
TURN_SPRITES = {
    (DOWN,  LEFT):  "body-turn-ld-dl",
    (LEFT,  DOWN):  "body-turn-ld-dl",
    (DOWN,  RIGHT): "body-turn-dr-rd",
    (RIGHT, DOWN):  "body-turn-dr-rd",
    (RIGHT, UP):    "body-turn-ur-ru",
    (UP,    RIGHT): "body-turn-ur-ru",
    (UP,    LEFT):  "body-turn-ul-lu",
    (LEFT,  UP):    "body-turn-ul-lu",
}