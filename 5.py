#lab 5 dict display
def display(list):
    t=0
    for i in list:
        print(str(list[i])+" "+str(i))
        t+=list[i]
    print("Total no. of items =",t)
inven={'rope':1,'torch':6,'goldcoin':42,'dagger':1,'arrow':12}
display(inven)
