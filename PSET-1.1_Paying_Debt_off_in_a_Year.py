balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 1

for month in range(1, 13):
    balance = balance - (balance * monthlyPaymentRate)
    balance = (1 + (annualInterestRate / 12)) * balance
#   print("Month ", month, " Remaining balance: ", round(balance, 2))

print("Remaining balance: ", round(balance, 2))
