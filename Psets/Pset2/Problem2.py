""""Fixed Monthly Payment to pay off debt"""
def lowpay(z=10):
     
     tbal = balance
     for i in range (12):
         
       ubal = tbal-z
       tbal = ubal + ubal *(annualInterestRate/12)
     
     if tbal <=0 :
         return z
     else :
         
         return lowpay(z + 10)
         
print('Lowest Payment:',lowpay())

