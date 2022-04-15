def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    c = 0
    for i in hand.keys() :
       if hand[i] != 0 :
        c += hand[i]
    return c
