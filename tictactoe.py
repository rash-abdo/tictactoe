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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for p in [X, O]:
        for i in range(3):
            if all(board[i][j] == p for j in range(3)) or all(board[j][i] == p for j in range(3)):
                return p
        if all(board[i][i] == p for i in range(3)) or all(board[i][2 - i] == p for i in range(3)):
            return p
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif all(cell is not None for row in board for cell in row ):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    def evaluation(board,p,alpha,beta,is_maximizing):
        if terminal(board):
            if winner(board) == p:
                return float('inf')
            elif winner(board) == None:
                return 0
            else:
                return float('-inf')
            
        elif is_maximizing:
            maxEval = -float('inf')
            for act in actions(board):
                eval = evaluation(result(board,act),p,alpha,beta,False)
                maxEval = max(maxEval,eval)
                alpha = max(alpha,eval)
                if beta<= alpha:
                    break
            return maxEval
        elif not is_maximizing:
            minEval = float('inf')
            for act in actions(board):
                eval = evaluation(result(board,act),p,alpha,beta,True)
                minEval = min(minEval,eval)
                beta = min(beta,eval)
                if beta <= alpha:
                    break
            return minEval            
        

    bestScore = -float('inf')
    move=(-1,-1)
    for act in actions(board): 
        score = evaluation(result(board,act),p,-9999,9999,False)
        if score>bestScore:
            bestScore=score
            move=act
    if move != (-1,-1):
        return move