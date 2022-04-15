"""Paying Debt off in a year"""
unbalance = 0

for i in range (12) :
    unbalance = balance - (balance*monthlyPaymentRate)
    balance = unbalance + (unbalance*(annualInterestRate/12))

    
print(round(balance,2))
