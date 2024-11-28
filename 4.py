#lab 4 spam display
def string(list):
    r=""
    for i in range(len(list)-1):
        r=r+list[i]+","
    print('"'+r,end=" ")
    print("and "+str(list[i+1])+'."')
spam=["apples","bananas","tofu","cats"]
string(spam)
