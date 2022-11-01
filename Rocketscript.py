from Rocket import RocketBoard

board = RocketBoard(2)

board[0].x = 4

print(board[0].get_distance(board[1]))
