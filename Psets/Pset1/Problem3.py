l = 0
crnt = s[0]
ans = s[0]

for i in range (len(s)-1) :
    if s[i+1] >= s[i] :
        crnt+= s[i+1]
        if len(crnt)> l:
            l = len(crnt)
            ans = crnt
    else :
        crnt=s[i+1]
    
print('Longest substring in alphabetical order is:', ans)
