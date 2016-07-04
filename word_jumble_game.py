#Word jumble
#the compiler picks a random word and then "jumbles" it
#the player has to guess the original word
#sarosh farhan- 08/03/2015

import random

#creat a sequence of words to choose from
words=("python","strontium","mercedes","rendezvous","coordinate","tabularize","enigma","refringent","forsakenness","jacobean","orthopedist","frequence","asphaltite","capucine","xylophone",)
#pick one word randomly from the sequence
word=random.choice(words)


#create a variable to use later to see if the guess is correct
correct=word

#create a jumbled version of the word
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position] + word[(position+1):]

#Start the game

print \
"""

                      WELCOME TO WORD JUMBLE!!!!
                UNSCRAMBLE THE LETTERS TO MAKE A WORD
        [IF YOU CANNOT GUESS,TYPE "GIVE UP" FOR CORRECT ANSWER]
              """
print "The jumble is :",jumble
guess=raw_input("\nYour guess:")
guess=guess.lower()
while (guess!=correct)and (guess!="give up"):
    print "Sorry,that's not it."
    guess=raw_input("Your guess:")
    guess=guess.lower()
if guess==correct:
    print "That's it!!!You guessed it!\n"
elif guess=="give up":
    print "oooh!!!poor little creature,answer is:",correct
print "Thanks for playing."
raw_input("\n\nPress the enter key to exit.")



