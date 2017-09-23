# CTI-110 
# M3HW1-Software Sales
# Name Alicia Campbell-Brown
# Date 9-24-2017


#Quantity 10-19: 10% discount
#Quantity 20-49:20% discount
#Quantity 50-99:30% discount
#Quantity 100+:	40% discount

 
userNumberofPackages = int( input( "Please enter the number of packages bought: " ) )

Priceofpackage = 99

if userNumberofPackages < 10:
    discount = 0;
elif userNumberofPackages < 20:
    discount = 0.10
elif userNumberofPackages < 50:
    discount = 0.20
elif userNumberofPackages < 100:
    discount = 0.30
    
else:
    discount = 0.40

subTotal = userNumberofPackages * Priceofpackage
discountAmount = discount * subTotal
total = subTotal - discountAmount

print( "\nAmount of Discount: $" + format( discountAmount, ",.2f" ) + \
       "\nTotal amount: $" + format(total, ",.2f" ) )
