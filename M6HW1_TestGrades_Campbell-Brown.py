# 11-11-2017
# CTI-110 M6HW1 - Test Average and Grade
# Alicia Campbell-Brown
#Write a program that asks the user to enter five test grades.
#The program should then display a letter grade for each score,
#and finally the average test score.
#Write the following functions for the program:
#main() – this function will control the main flow of the program.

#calc_average() – this function should accept five test scores (int or float)
#as arguments, and return the average of the scores.

#determine_grade() –
#This function should accept a test score (int or float) as an argument
#and return a letter grade for the score.

#Score  Letter Grade
#90-100      A
#80-89       B
#70-79       C
#60-69       D
#Below 60    F


def calcAverage( score1, score2, score3, score4, score5 ):
    average = ( score1 + score2 + score3 + score4 + score5 ) / 5
    return average

def determineGrade( userScore ):
    if( userScore < 60 ):
        return "F"
    elif( userScore < 70 ):
        return "D"
    elif( userScore < 80 ):
        return "C"
    elif( userScore < 90):
        return "B"
    elif( userScore < 101):
        return "A"

def askForScores():
    score1 = float( input( "Please enter score 1: " ) )
    score2 = float( input( "Please enter score 2: " ) )
    score3 = float( input( "Please enter score 3: " ) )
    score4 = float( input( "Please enter score 4: " ) )
    score5 = float( input( "Please enter score 5: " ) )

    return score1, score2, score3, score4, score5
                    



def printTableOfResults( score1, score2, score3, score4, score5 ):
    print( "Score\tLetter Grade" )
    print( str( score1 ) + "\t\t" + determineGrade( score1 ), \
           str( score2 ) + "\t\t" + determineGrade( score2 ), \
           str( score3 ) + "\t\t" + determineGrade( score3 ), \
           str( score4 ) + "\t\t" + determineGrade( score4 ), \
           str( score5 ) + "\t\t" + determineGrade( score5 ), sep = "\n" )
    
def main():
    score1, score2, score3, score4, score5 = askForScores()
    print()
    printTableOfResults( score1, score2, score3, score4, score5 )
 
main() 
 
    

    
