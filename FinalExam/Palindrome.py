def isPalindrome(aString):
    aString = aString.lower()
    a = len(aString)
    
     
    
    if a < 2:
        return True
 
    
    elif aString[0] == aString[a-1]:
        
        
        return isPalindrome(aString[1: a - 1])
 
    else:
        return False
