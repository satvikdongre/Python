#lab 6a identify longest word
def main():
    text=input("Enter the list of words:")
    l=0
    for w in text.split():
        if len(w)>l:
            l=len(w)
            lw=w
    print("The longest word among all is "+lw+" with %d letters"%l)
main()
