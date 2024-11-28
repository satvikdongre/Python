mil=int(input("Enter the mileage:"))
amt=int(input("Enter the amt of fuel per litre:"))
dist=int(input("Enter the distance one way:"))
per=((dist*2)/mil*amt)/6
if per%3==0:
    print(True)
    print("Per head cost is", per)
else:
    print(False)
    print("Per head cost is", per)
