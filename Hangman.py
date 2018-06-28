import random
HANGMAN = ('''
  +---+   
  |   | 
  |   |
      |
	  |
=========''', '''
  +---+
  |   |
  O   |
      |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
#max number of wrong guesses can a player can make
MAX_WRONG = len(HANGMAN) - 1
#tuple list of words that user can guess 
WORDS = ("ANIMAL", "CHICKEN", "PYTHON", "OWL", "NOODLES", "BIRIYANI", "DATA NETWORKING")

#initiate the variables
word = random.choice(WORDS)

so_far = "_" * len(word)

wrong = 0

used = []

print ("welcome to Hangman. Good Luck")

while wrong < MAX_WRONG and so_far != word:
    print (HANGMAN[wrong])
    print ("\nyou have used the following letters:\n", used)
    print ("\nso far, the word is:\n", so_far)
    guess = input("Enter your guess")
    guess = guess.upper()

    while guess in used:
        print ("you have already guessed the letter:", guess)
        guess = input("Enter a guess: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print ("\nYes", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[1]:
                new += guess
            else:
                new += so_far[1]
        so_far = new
    else:
        "\nSorry,", guess, "isn't in the word"
        wrong += 1

if wrong == MAX_WRONG:
    print (HANGMAN[wrong])
    print ("\nYou have been hanged!")
else:
    print ("\nYou guessed it!")
print ("\nThe word was", word)

input("\n\nPress the enter key to exit.")
