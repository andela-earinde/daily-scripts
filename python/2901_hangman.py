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
    import string

    guessesLeft = 8
    mistakesMade = 0
    lettersGuessed = []
    availableLetters = string.ascii_lowercase

    print "Loading word list from file..."
    print "55900 words loaded."
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + len(secretWord) + " letters long."
    print "-------------"

    while not isWordGuessed(secretWord, lettersGuessed):
      if guessesLeft <= 0:
        print "Sorry, you ran out of guesses. The word was " + secretWord
        return False

      print "You have " + str(guessesLeft) + " guesses left."
      print "Available letters: " + availableLetters

      usersGuess = raw_input('Please guess a letter: ')
      if userguess in lettersGuessed:
        print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
      else:
        if userGuess in secretWord:
          lettersGuessed.append(userGuess)
          availableLetters = getAvailableLetters(lettersGuessed)

          print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
        else:
          lettersGuessed.append(userGuess)
          availableLetters = getAvailableLetters(lettersGuessed)
          mistakesMade += 1
          guessesLeft -= 1

          print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)

    print "Congratulations, you won!"





