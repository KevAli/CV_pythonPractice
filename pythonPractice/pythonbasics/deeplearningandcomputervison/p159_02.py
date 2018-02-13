moves = ['up', 'left', 'down', 'right']
coord = [0, 0]
for move in moves:
    if move == 'up':
        coord[1] += 1
    elif move == 'down':
        coord[1] -= 1
    elif move == 'left':
        coord[0] -= 1
    elif move =='right':
        coord[0] += 1
    else:
        pass
    print(coord)


