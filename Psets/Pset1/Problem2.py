ctr=0
ptr = 0
x=0
y=3
#print(s[0:3])

while ptr < len(s):
  
  ans = s[x:y]
  
  
  if ans == 'bob' :
      ctr += 1
      x += 1
      y += 1
     
    
  else :
      x += 1
      y += 1
     
     
  ptr += 1
      
      
print('Number of times bob occurs is: '+ str(ctr))

