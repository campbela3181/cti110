##CTI 110
#M6T1-Kilometer Converter
#Alicia Campbell-Brown
#11-11-2017
#Write a program that asks the user to enter a distance in kilometers,
#and then converts that distance to miles.
#This is the conversion formula:
#Miles = Kilometers * 0.6214


def askUserForKilometers():
#Get the distance in kilometers
    userKilometers = float( input( "Please enter the distance" + \
                                   " in kilometers: " ) )
    return userKilometers

def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( userKilometersTyped )

    print()

    print( userKilometersTyped, "kilometers converted to miles is", \
           format( convertedMiles, ".2f"), "miles" )


main()

    
    
