import random
import ps3_hangman

#print(chooseWord(wordlist))

from ps3_hangman import *
secretWord = chooseWord(wordlist)
#print(secretWord)

print("Welcome to the game, Hangman!")
print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
print("-------------")

guessesLeft = 8
avlLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersGuessed = ''
hiddenWord = []

while guessesLeft > 0:
    print('You have ' + str(guessesLeft) + ' guesses left.')
    print("Available letters: " + ''.join(avlLetters))
    guess = ps3_hangman.get_guess(avlLetters)
    
    hiddenWord = ps3_hangman.getGuessedWord(hiddenWord, secretWord, lettersGuessed, guess)
    lettersGuessed = lettersGuessed + guess
    avlLetters = ps3_hangman.removeFromAvl(avlLetters, guess)
    if guess in secretWord:
        print('Good guess: ' + ' '.join(hiddenWord))
        input()
        if isWordGuessed(secretWord, hiddenWord) == True:
            print("------------")
            print('Congratulations, you won!')
            break
    else:
        print("Oops! That letter is not in my word: " + ' '.join(hiddenWord))
        input()
        guessesLeft -= 1
        ps3_hangman.print_hangman(guessesLeft)
    print("------------")

if guessesLeft == 0:
    print('Sorry, you ran out of guesses. The word was else.')
    print('The word was ' + secretWord)
