#hangman game
#10/9/19
#Taya Martinez

##the classic game of hangman
##the computer picks random word
##and the player trys to guess it,
##one letter at a time. If the player
##can't guess the word in time, the little
##stick figure gets hung.

#imports
import random

#constants
HANGMAN=(
"""    _______
      |/         |
      |         
      |        
      |          
      |     
      |
___|___""",
"""    _______
      |/         |
      |         (_)
      |        
      |          
      |         
      |
___|___""",

"""    _______
      |/         |
      |         (_)
      |          |
      |          |
      |         
      |
___|___""",
"""    _______
      |/         |
      |         (_)
      |        /|
      |          |
      |         
      |
___|___""",

"""    _______
      |/         |
      |         (_)
      |        /|\\
      |          |
      |         
      |
___|___""",
"""    _______
      |/         |
      |         (_)
      |        /|\\
      |          |
      |         /  
      |
___|___"""
"""    _______
      |/         |
      |         (_)
      |        /|\\
      |          |
      |         / \\
      |
___|___""")

MAX_WRONG=len(HANGMAN)-1
WORDS=("OVERUSED", "CLAM", "GUAM", "TAFFETA","PYTHON")

word=random.choice(WORDS)#guessed word
so_far="-" *len(word) #one dash per letter
wrong= 0#number of wrong guesses made
used=[]#letters already guessed

print("Welcome to Hangman. Good Luck!")

while wrong<MAX_WRONG and so_far !=word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters: \n",used)
    print("\nSo far, the word is:\n", so_far)

    guess=input("\n\nEnter your guess: ")
    guess= guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess=input("\n\nEnter your guess: ")
        guess= guess.upper()
        
    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new=""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far=new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong += 1

if wrong== MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hung!")
else:
    print("\nYou guessed it!")
print("\nThe word was",word)
print("\n\nPress the enter key to exit.")
