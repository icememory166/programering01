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

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tileToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # keep moving in this direction
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space,
                # noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tileToFlip.append([x, y])
    if len(tileToFlip) == 0: # If no tiles were flipped, this is not a valid move
        return False
    return tileToFlip

def isOnBoard(x, y):
    # Return True if the coordinates are located on the board
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):
    # Return a new board with periods marking the valid moves the player can make.
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given player on the given board
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Return a dictionary with keys 'X' and 'O'
    xscore = 0
    yscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                yscore += 1
    return {'X':xscore, 'O':yscore}

def enterPlayerTile():
    # Let the player enter which tile they want to be
    # Return a list with the player's tile as the first item and the computer's tile as the sceond
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    # The first element in the list is the player's tile, and the second is the computer's tile
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # randomly choose who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    # place the tile on the board at xstart, ystart and flip any of the opponent's tiles.
    # Return False if this move is an invaled move; True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    # make a duplicate of the board list and return it
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

            return boardCopy

def isOnCorner(x, y):
    # Return True if the position is in one of the four corners
    return (x == o or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getPlayerMove(board, playerTile):
    # let the player enter their move
    # Return the move as [x, y] (or return the strings 'hints' or 'quit')
    DIGITS0TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) == 2 and move[0] in DIGITS0TO8 and move[1] in DIGITS0TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break        
