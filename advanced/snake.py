from settings import (
    UP, DOWN, RIGHT, LEFT,
    OPPOSITE, CELL_SIZE, TURN_SPRITES,
    GRID_HEIGHT, GRID_WIDTH
)

from helpers import get_direction, direction_name

class Snake:
    def __init__(self):
        self.body = [
            (9, 6),
            (9,  7),
            (10,  7),
        ]
        self.direction = LEFT
        self.grow      = False

    def set_direction(self, new_direction):
        if new_direction != OPPOSITE[self.direction]:
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def check_collision(self):
        head_x, head_y = self.body[0]

        # wall collision
        if (
            head_x < 0 or
            head_x >= GRID_WIDTH or
            head_y < 0 or
            head_y >= GRID_HEIGHT
        ):
            return True

        # self collision
        if self.body[0] in self.body[1:]:
            return True

        return False

    # ===== DRAW =====
    def draw(self, screen, sprites):
        for i, segment in enumerate(self.body):
            x, y     = segment
            draw_pos = (x * CELL_SIZE, y * CELL_SIZE)

            # HEAD
            if i == 0:
                direction = get_direction(self.body[0], self.body[1])
                sprite_name = f"head-{direction_name(direction)}"
                screen.blit(sprites[sprite_name], draw_pos)

            # TAIL
            elif i == len(self.body) - 1:
                direction = get_direction(self.body[-2], self.body[-1])
                sprite_name = f"tail-{direction_name(direction)}"
                screen.blit(sprites[sprite_name], draw_pos)

            # BODY
            else:
                prev_seg = self.body[i - 1]
                next_seg = self.body[i + 1]

                dir_prev = get_direction(prev_seg, segment)
                dir_next = get_direction(next_seg, segment)

                # straight
                if dir_prev in (LEFT, RIGHT) and dir_next in (LEFT, RIGHT):
                    sprite = sprites["body-horizontal"]
                elif dir_prev in (UP, DOWN) and dir_next in (UP, DOWN):
                    sprite = sprites["body-vertical"]
                # turn
                else:
                    sprite = sprites[TURN_SPRITES[(dir_next, dir_prev)]]

                screen.blit(sprite, draw_pos)