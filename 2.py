a=int(input("Enter the number:"))
print(a,end=" ")
while a!=1:
    if a%2==0:
        a=a//2
    else:
        a=3*a+1
    print(a,end=" ")
