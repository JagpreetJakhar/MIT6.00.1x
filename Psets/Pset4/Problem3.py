def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    b = False
    c = 0
    hand3 = hand.copy()
    
    if word in wordList :
       
        for i in word :
            if i in hand3.keys() and  (hand3[i] != 0) : 
                 
                     c+=1
                     hand3[i] = hand3[i]- 1

        if c == len(word):
            b = True
          
    return b
