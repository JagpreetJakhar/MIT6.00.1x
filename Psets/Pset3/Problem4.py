def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secretWord), 'letters long.')
    print ("-----------")
    guesses = 8
    var_s=''
    lettersGuessed=[]
    while guesses >0 or isWordGuessed(secretWord, lettersGuessed) == False :
          
              
          print('You have ',guesses,'guesses left.')
          print('Available letters:',getAvailableLetters(lettersGuessed))
          var_s = input('Please guess a letter :').lower()
           
          
          if var_s in lettersGuessed :
             print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
             print ("-----------")
             var_s=''
             
          if var_s not in lettersGuessed and var_s != '' :
              if var_s in secretWord :
                 lettersGuessed+=var_s
                 print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
                 print ("-----------")
                 var_s=''
                 
              if var_s not in secretWord :
                 lettersGuessed+=var_s
                 print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
                 print ("-----------")
                 guesses = guesses-1
                 var_s =''
                 
          if guesses <=0 :
             print('Sorry, you ran out of guesses. The word was',secretWord,'.')
             break
          if isWordGuessed(secretWord, lettersGuessed) == True :
             print('Congratulations, you won!')
             break
          
