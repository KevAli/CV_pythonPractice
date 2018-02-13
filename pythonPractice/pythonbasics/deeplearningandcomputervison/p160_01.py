moves = ['up', 'left', 'down', 'right']


def move_up(x):
    x[1] += 1


def move_down(x):
    x[1] -= 1


def move_left(x):
    x[0] -= 1


def move_right(x):
    x[0] += 1


actions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}
coord = [0, 0]
for move in moves:
    actions[move](coord)
    print(coord)
