import random
HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
   [O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
   [O]  |
   /|\  |
   / \  |
       ===''']
words = {'Colors':'''red orange yellow green blue indigo violet white black
      brown'''.split(),
'Shapes':'''square triangle rectangle circle ellipse rhombus trapezoid
      chevron pentagon hexagon septagon octagon'''.split(),
'Fruits':'''apple orange lemon lime pear watermelon grape grapefruit cherry
      banana cantaloupe mango strawberry tomato'''.split(),
'Animals':'''bat bear beaver cat cougar crab deer dog donkey duck eagle
      fish frog goat leech lion lizard monkey moose mouse otter owl panda
      python rabbit rat shark sheep skunk squid tiger turkey turtle weasel
      whale wolf wombat zebra'''.split()}

def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary of lists of strings and its key.
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex =random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey] [wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #Replace blanks with correcly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        for letter in blanks: #Show the secret word with spaces in between each letter.
            print(letter, end=' ')
        print()

def getGuess(alreadyGuessed):
    # returns the letter the player entered. this function makes sure the player
    # entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # this function returns True if the player wants to pla yagain;
    # otherwise, it returns False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    #Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is" {secretWord}" you have won, but at what cost?')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

    # check if player has guessed too many times and lost.
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter' + str(len(missedLetters)) + 'missed guesses and ' + str(len(correctLetters)) + f'correct guesses, the word was "{secretWord}"')
        gameIsDone = True
    #Ask the player if they want to play again (but only if the game is done.)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
