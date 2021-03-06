def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    store = {}
    usr = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
    while usr != 'e' :
        if usr == 'n' :
            hand = dealHand(HAND_SIZE)
            store = hand
            playHand(hand, wordList,HAND_SIZE )
            usr = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        elif usr == 'r' :
            if len(store) == 0 :
                print('You have not played a hand yet. Please play a new hand first!')
                usr = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
               
            else :
                
                playHand(store, wordList,HAND_SIZE )
                usr = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        
        else :
            print('Invalid command.')
            usr = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
    
    
