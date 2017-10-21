# CTI 110
#M5HW3- Factorial
#Alicia Campbell-Brown
#10-20-2017


def main():

    n = int(input('Enter a nonnegative integer? ' ))
    fact = 1
    i = 2
    if n < 0:
        print ("Sorry you must inter a nonnegative number")
    else:
        while i <= n:
            fact = fact * i
            i = i + 1
        print("The factorial of", n , "is" ,fact)

main()

        
    
    
