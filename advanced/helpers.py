from settings import UP, DOWN, LEFT, RIGHT

def get_direction(a, b):
    dx = a[0] - b[0] # x1 - x2
    dy = a[1] - b[1] # y1 - y2
    return (dx, dy)

def direction_name(direction):
    names = {
        UP:    "up",
        DOWN:  "down",
        LEFT:  "left",
        RIGHT: "right",
    }
    return names[direction]