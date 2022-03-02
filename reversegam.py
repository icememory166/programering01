# Reversegam: a clone of Othello/Reversi
import random
import sys
WIDTH = 8 # board is 8 spaces wide
HEIGHT = 8 # board is 8 spaces tall
def drawBoard(board):
    # Print the board passed to the function. REturn None
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    # Create a brand-new, bland board data structure
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # Return False if the player's move on space xstart, ystart is invalid
    # If it is a valid move, return a list of spaces that would become the player's if they made a move here
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False                        
