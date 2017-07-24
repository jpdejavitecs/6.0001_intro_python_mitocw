balance = 4060

annualInterestRate = 0.04

lowestPayment = 0
auxBalance = balance

guess = balance // 12
guessEnd = (balance * (1 + annualInterestRate)) // 12

while guess <= guessEnd:
    month = 12
    while month > 0:
        if month == 12:
            balance = int(balance - guess)
            month -= 1
        else:
            balance = int(balance * (1 + (annualInterestRate / 12)) - guess)
            month -= 1
    if balance < 1:
        lowestPayment = int(guess)
        while lowestPayment % 10 != 0:
            lowestPayment += 1
        break
    balance = auxBalance
    guess += 1
    
print("Lowest Payment: ", lowestPayment)
