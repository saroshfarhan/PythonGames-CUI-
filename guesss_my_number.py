print"                           Welcome to guess my number"
print"                                                                      "
print"                  I am thiking of a number between 1 and 100."
print"                                                                       "
print"                Try to guess it in as few attempts as possible."
import random
#set the initial values
the_number=random.randrange(100)+1
guess=int(raw_input("Take a guess: "))
tries=1
#guessing loop
while (guess!=the_number):
    if (guess>the_number):
        print "Lower....."
    else:
        print "Higher...."
    guess=int(raw_input("Take a guess: "))
    tries=tries+1
print "You guessed it!!! The number was", the_number
print "And it only took you ",tries,"tries!"
raw_input("Press enter key to exit.")
