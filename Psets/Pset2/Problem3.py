#Using Bisection to make program faster
mtr = annualInterestRate/12
low = balance /12
upper = (balance*((1+mtr)**12))/12



tbal = balance
while tbal !=0 :
      ans = (low + upper)/2
      unbal = 0
      intr = 0
      tbal = balance
