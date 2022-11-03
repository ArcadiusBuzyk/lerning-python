from Rocket import RocketBoard

board = RocketBoard(2)

board[0].x = 4

print(board.get_distance(board[0], board[1]))
