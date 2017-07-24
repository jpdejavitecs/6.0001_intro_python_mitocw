# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

#----------------------------------------------
#Start of my codes


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #se falso, diminuirá uma chance e terá mais uma rodada
    #else: retorna que o usuário ganhou
    checkAns = ''
    for i in range(0, len(lettersGuessed)):
        if lettersGuessed[i] in secretWord:
            #pedir o index, por no lugar do array, dar um JOIN para converter para string e comparar
            checkAns = str(checkAns) + str(secretWord[i])
    
    return checkAns == secretWord



def getGuessedWord(hiddenWord, secretWord, lettersGuessed, guess):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    u = "_"
    if len(lettersGuessed) == 0:
        for i in range(0, len(secretWord)):
            if guess == secretWord[i]:
                hiddenWord.append(guess)
            else:
                hiddenWord.append(u)   
    else:
        for i in range(0, len(secretWord)):
            if guess == secretWord[i] and hiddenWord[i] == u:
                hiddenWord[i] = guess
            
    return hiddenWord
        


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

def removeFromAvl(avlLetters, guess):
    for n in range(0, len(avlLetters)):
        if guess == avlLetters[n]:
            del avlLetters[n]
            break
    return avlLetters

def get_guess(avlLetters):
    guess = str(input('Please guess a letter: '))
    if guess not in avlLetters:
        print("Oops! You've already guessed that letter!")
        return get_guess(avlLetters)
    else:
        return guess
        

def print_hangman(guessesLeft):
    if guessesLeft == 7:
        print('_______')
        print('|            |')
        print('|          (_)')
        print('|')
        print('|')
        print('|')
    elif guessesLeft == 6:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|           | ')
        print('|           |')
        print('|')
    elif guessesLeft == 5:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|         /| ')
        print('|           |')
        print('|')
    elif guessesLeft == 4:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|         /|\ ')
        print('|           |')
        print('|')
    elif guessesLeft == 3:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|         /|\ ')
        print('|           |')
        print('|          /')
    elif guessesLeft == 2:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|         /|\ ')
        print('|           |')
        print('|          /\ ')
    elif guessesLeft == 1:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|         /|\ ')
        print('|           |')
        print('|        _/\ ')
    elif guessesLeft == 0:
        print('_______')
        print('|           |')
        print('|         (_)')
        print('|         /|\ ')
        print('|           |')
        print('|        _/\_')
