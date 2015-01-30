#!/usr/bin/python

import random

class HangmanGame:
  def start(self, secretWord):
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

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-------------"

    while not self.isWordGuessed(secretWord, lettersGuessed):
      if guessesLeft <= 0:
        print "Sorry, you ran out of guesses. The word was " + secretWord
        return False

      print "You have " + str(guessesLeft) + " guesses left."
      print "Available letters: " + availableLetters

      # Obtain the user's guess
      userGuess = raw_input('Please guess a letter: ').lower()

      if userGuess in lettersGuessed:
        print "Oops! You've already guessed that letter: " + self.getGuessedWord(secretWord, lettersGuessed)
      else:
        if userGuess in secretWord:
          lettersGuessed.append(userGuess)
          availableLetters = self.getAvailableLetters(lettersGuessed)

          print "Good guess: " + self.getGuessedWord(secretWord, lettersGuessed)
        else:
          lettersGuessed.append(userGuess)
          availableLetters = self.getAvailableLetters(lettersGuessed)
          mistakesMade += 1
          guessesLeft -= 1

          print "Oops! That letter is not in my word: " + self.getGuessedWord(secretWord, lettersGuessed)

    print "Congratulations, you won!"

  def getGuessedWord(self, secretWord, lettersGuessed):
    '''
    secretWord: string, the secret word in the game
    lettersGuessed: list, a collection of the letters a user has already guessed

    returns string

    Displays the secretWord, showing what letters have been guessed and hiding others by replacing them with underscores.
    '''
    result = secretWord
    for char in secretWord:
      if char not in lettersGuessed:
        result = result.replace(char, '_')

    return result

  def getAvailableLetters(self, lettersGuessed):
    '''
    lettersGuessed: list, a collection of the letters the user has already guessed

    returns string

    Displays what letters of the alphabet are yet to be used in the current session of the Hangman game.
    '''
    import string

    alphabet = string.ascii_lowercase
    for char in lettersGuessed:
      alphabet = alphabet.replace(char, '')

    return alphabet

  def isWordGuessed(self, secretWord, lettersGuessed):
    '''
    secretWord: string, the secret word in the game
    lettersGuessed: list, a collection of the letters the user has already guessed

    returns boolean

    Determines if the user has guessed the secret word i.e all the characters in the secretWord are in the lettersGuessed list.
    '''
    result = True
    for char in secretWord:
      if char not in lettersGuessed:
        result = False

    return result

sampleWords = [
  'anatagonistic',
  'bacchanalia',
  'cryptographic',
  'dessication'
]

word = random.choice(sampleWords)

game = HangmanGame()
game.start(word)





