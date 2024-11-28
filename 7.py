#lab 7 pattern Name
import re
def val(name):
    regex=re.compile(r"^(Mr|Mrs|Ms)\.\s([a-zA-Z]+)\s?([a-zA-Z]+)?\s?([a-zA-Z]+)?")
    b=regex.search(name)
    if b:
        return True
    else:
        return False
n=input("Enter ur name(e.g., Mr. John Smith or Mrs. Jane E smith:)")
if val(n):
    print("Valid name")
else:
    print("Invalid name")
