# Sonar Tresure Hunt

import random, sys, math



def getNewBoard():
    # Create a new 60x15 board data structure
    board = []
    for x in range(60): # the main list is a list of 60 lists
        board.append([])
        for y in range(15): # each list in the main list has 15 single character strings
