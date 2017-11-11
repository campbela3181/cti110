# 11-11-2017
# CTI-110 M6T2_FeetToInches 
# Alicia Campbell-Brown
#Write a program that asks the user to enter a distance in feet,
#and prints that same distance in inches. 
#This is the conversion formula, of course:
#Inches = Feet * 12


def feetToInches( userFeet ):
    inches = ( userFeet / 1 ) * 12
    return inches

def main():
    userFeet = float( input( "Please enter the number of feet: " ) )
    print()
    inches = feetToInches( userFeet )
    print( userFeet, "feet converted to inches is", format( inches, ".2f" ),\
           "inches" )

main()
