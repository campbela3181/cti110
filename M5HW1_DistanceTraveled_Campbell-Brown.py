#CTI 110
#M5HW1-Distance Traveled
#Alicia Campbell-Brown
#10-20-2017
#Write a program that asks the user two questions: The speed of a vehicle,
#and the number of hours it has traveled.
#The program should then display the distance that the vehicle has traveled for each hour of that time period.
#Your output should be displayed in table format.

#distance = speed * time

#What is the speed of the vehicle in mph? 40
#How many hours has it traveled? 3
#Hour		Distance Traveled
#---------------------------
#1		40	
#2		80
#3		120


vehicleSpeed = float(input( "What is the speed of the vehicle:" ) )
timeTraveled = int(input( "How many hours has it traveled?: " ) )

print()

print( "Hour","\tDistance Traveled" )
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour,"\t",distanceTraveled,)
