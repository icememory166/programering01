# tic-tac-toe

import random

def drawBoard(board):
    # this function writes out the board that it was passed

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    # lets the player input which letter they want to be
    # returns a list with the player's letter as the first item and the computer's letter as the second
    letter = ''
    while not (letter =='X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # the first element in the list is the player's letter; the second is the computer's letter
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # randomly choose which player goes First
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # given a board and a player's letter, this fucntion returns True if that player has won
    # we use "bo" instead of board and "le" instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
    # make a copy of the board list and return it
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board,move):
    # return True if the passed move is free on the board
    return board[move] == ' '

def getPlayerMove(board):
    # let the player enter their own move
    move = ' '
    while not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

        
