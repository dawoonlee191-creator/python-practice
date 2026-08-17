Bill=float(input("How much is the bill?"))
Tip=float(input("tip percentage (10, 15, 20)?"))
Finaltip=Bill*(Tip/100)
Finalbill=Bill+Finaltip 
print("Tip amount:$"+str(Finaltip))
print("Total bill:$"+str(Finalbill))
