choice=int(input("press 1 for for km → miles and 2 for miles → km >"))
value=float(input("Enter the value you want to convert"))
if choice==1:
    miles=value* 0.621371
    print("The value in miles is: "+str(miles))
else:
    km=value* 1.60934
    print("The value in km is: "+str(km))
