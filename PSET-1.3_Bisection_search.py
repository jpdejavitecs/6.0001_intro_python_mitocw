balance = 320000

annualInterestRate = 0.2

lowestPayment = 0
auxBalance = balance
epsilon = 1 #fator de proximidade

low = balance // 12
high = (balance * (1 + annualInterestRate)) // 12

ans = (high + low) / 2.0

while lowestPayment == 0: #PROBLEMA
    balance = auxBalance
    month = 12
    while month > 0:
        if month == 12:
            balance = int(balance - ans)
            month -= 1
        else:
            balance = int(balance * (1 + (annualInterestRate / 12)) - ans)
            month -= 1
    if balance == 0: #< epsilon and balance > -epsilon
        lowestPayment = ans
        break
    elif balance < 0:
        high = ans
        ans = (high + low) / 2.0
    else:
        low = ans
        ans = (high + low) / 2.0
    
print("Lowest Payment: ", round(lowestPayment + 0.5, 2))

#MARGEM DE ERRO 0.2
