
# CTI-110 
# M2HW2 - Tip Tax Total 
# Alicia Campbell-Brown
# 9-10-2017


foodCharge = float( input( "Please enter the charge of the food: " ) )
tip = 0.18 * foodCharge
salesTax = 0.07 * foodCharge
total = foodCharge + tip + salesTax

print( "Food Charge: $" + format( foodCharge, ",.2f"), "Tip: $" + \
       format( tip, ",.2f" ), "Salex Tax: $" + format( salesTax, ",.2f"), \
       "Total: $" + format( total, ",.2f"), sep = "\n" )
