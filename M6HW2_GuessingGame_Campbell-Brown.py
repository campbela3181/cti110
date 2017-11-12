# 11-12-2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Alicia Campbell-Brown
#
#Generate a random number in the range of 1 through 100.
#Ask the user to guess what the secret number is.
#If the user’s guess is higher than the secret number,
#the program should tell the user Too high, try again.
#If the user’s guess is lower than the secret number,
#the program should tell the user Too low, try again.
#If the user guesses the number correctly,
#the program should congratulate the user!
#Write whatever message you think is appropriate for this case.
#The program should then ask the user Play again? (y for yes).
#if the user enters ‘y’, then the program should generate a new random number
#and start the game over again.


import random

def generateRandomNumber():
    randomNumber = random.randint( 1, 100)
    return randomNumber

def askUserForNumber( message = "Guess the number: " ):
    userNumber = int( input( message ) )
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "Congratulations!"

def main():
    print()
    userCongratulated = False
    letsStart = True 

    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        userNumberofGuesses = userNumberOfGuesses + 1
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print( message)
            userNumber = askUserForNumber( "Try again" )
            userNumberOfGuesses = userNumberOfGuesses + 1 
            message = checkUserNumber( userNumber, randomNumber )
            
        print()
        print( message, "It took you", userNumberOfGuesses, \
               " attempts to guess correctly\n")
        print( "Play Again" )
        userCongratulated = True

main()        
        
    
     
    
    
    
    
