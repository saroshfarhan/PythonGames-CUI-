#Hangman Game
#Sarosh Farhan-08/03/2015

#imports
import random

#constants
HANGMAN=(
"""
   ----

   |     |
   |
   |
   |
   |
   |
   |
   |
  -----------
"""
  ,
"""
   ----
  |     |
  |     O
  |
  |
  |
  |
  |
  |
 --------------
"""
  ,
"""
    ----
   |     |
   |     O
   |    -+-
   |
   |
   |
   |
   |
  --------------
"""
  ,
"""
     ----
    |     |
    |     O
    |   /-+-
    |
    |
    |
    |
    |
   --------------
"""
   ,
"""
     ----
    |     |
    |     O
    |   /-+-/
    |
    |
    |
    |
    |
   --------------
"""
   ,
"""
     ----
    |     |
    |     O
    |   /-+-/
    |     |
    |
    |
    |
    |
   --------------
"""
   ,
"""
     ----
    |     |
    |     O
    |   /-+-/
    |     |
    |     |
    |    |
    |    |
    |
   --------------
"""
   ,
"""
     ----
    |     |
    |     O
    |   /-+-/
    |     |
    |     |
    |    | |
    |    | |
    |
   --------------
""")

MAX_WRONG=len(HANGMAN)-1
WORDS=("OVERUSED","CLAM","PRITAM","RAHUL","DHOOM")

#Initializing variables
word=random.choice(WORDS)
so_far="-"*len(word)
wrong=0
used=[]
print "WELCOME TO HANGMAN.GOOD LUCK!!!"
while(wrong<MAX_WRONG)and(so_far!=word):
    print HANGMAN[wrong]
    print"\nYou've used the following letters:\n",used
    print "\nSo far,the word is:\n",so_far
    guess=raw_input("\n\nEnter your guess: ")
    guess=guess.upper()
    while (guess in used):
        print "You've already guessed the letter:",guess
        guess=raw_input("Enter your guess: ")
        guess=guess.upper()
    used.append(guess)
    if (guess in word):
        print "\nYes!!!",guess,"is the word!!!"
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far=new
    else:
        print "\nSorry",guess,"isn't in the word."
        wrong+=1

#Ending the game
if (wrong==MAX_WRONG):
    print HANGMAN[wrong]
    print "\nYou've been hanged!!"
else:
    print "\nYou guessed it!!"
print "\nThe word was",word
raw_input("\n\nPress the enter key to exit.")
