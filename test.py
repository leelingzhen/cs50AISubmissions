from tictactoe import player,actions,result,winner,terminal,utility,maxUtility,minUtility

X = "X"
O = "O"
EMPTY = None

# test_board = [[X, X, None], [O, O, O], [None, X, None]]
# print(terminal(test_board))




test_board = [[X, EMPTY, EMPTY],
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
# print(result(test_board,(0,1)))
print('testing maximumUtility')
print(minUtility(test_board))