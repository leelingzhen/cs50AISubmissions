"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): # terminal board not considered
    count = 0
    for i in board:
        for j in i:
            count += 1 if j != None else 0
    
    return X if count%2 == 0 else O

    # raise NotImplementedError


def actions(board): #terminal board not considered
    setActions = set() 
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                setActions.add((i,j))
    return setActions


def result(board, action): #terminal board not considered
    possibleMoves = actions(board)
    currentMove = player(board)
    if action not in possibleMoves:
        raise 'InvalidMove'
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = currentMove
    return newBoard
    


def winner(board):
    for i in range(3): #horizontal Check
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i] #vertical check
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board [0][0]
    elif board [0][2] == board [1][1] and board[1][1] == board[2][0]:
        return board [0][2]
    else:
        return None


def terminal(board):
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == None:
                return False
    return True
    

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = maxUtility(board)
            return move
        else:
            value, move = minUtility(board)
            return move


def maxUtility(board):
    if terminal(board):
        return utility(board), None

    value = -999
    optimalMove = None
    for move in actions(board):
        # v = max(v, min_value(result(board, action)))
        newValue, m = minUtility(result(board, move))
        if newValue > value:
            value = newValue
            optimalMove = move
            if value == 1:
                return value, optimalMove

    return value, optimalMove


def minUtility(board):
    if terminal(board):
        return utility(board), None

    value = 999
    optimalMove = None
    for move in actions(board):
        #  v = Min(v, Max-Value(Result(state, action)))
        newValue, m = maxUtility(result(board, move))
        if newValue < value:
            value = newValue
            optimalMove = move
            if value == -1:
                return value, optimalMove

    return value, optimalMove