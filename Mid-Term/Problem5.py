def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    l = []
    ldic=[]
    ldic = list(aDict.values())
    for i, j in aDict.items() :
        if ldic.count(j)==1:
            l.append(i)
    
  
      
        
    return l 
          
