
def getGuessedWord(hiddenWord, secretWord, lettersGuessed, guess):
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

def isWordGuessed(secretWord, hiddenWord):
    #se falso, diminuirá uma chance e terá mais uma rodada
    #else: retorna que o usuário ganhou
    return ''.join.(hiddenWord) == secretWord



hiddenWord = []
secretWord = 'basketball'
lettersGuessed = ''
guess = 'b'
hiddenWord = getGuessedWord(hiddenWord, secretWord, lettersGuessed, guess)
lettersGuessed = lettersGuessed + guess
isWordGuessed(secretWord, lettersGuessed)
guess = 'l'
hiddenWord = getGuessedWord(hiddenWord, secretWord, lettersGuessed, guess)
