#CTI 110
#M5HW2-Running Total
#Alicia Campbell-Brown
#10-20-2017



def main():

    # declaring and intializing the variables.

    runningTotal = 0
    number = 0

    # Setting up the while loop to add numbers until a negative one is entered.

    while number >= 0:
        number = int(input('Enter a positive number: '))

    # Check if the number is positive so it doesn't change the running total value.

        if number >= 0:
            runningTotal = runningTotal + number
            
            print()

    # Display the running total.

    print()
    print ('Total = ' ,runningTotal,)


main()
