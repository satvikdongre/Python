import random
a=random.randint(1,20)
print("Random number lies between 1 to 20")
for i in range(1,7):
    b=int(input("Enter ur guess:"))
    if b<a:
        print("Your guess is low")
    elif b>a:
        print("Your guess is high")
    else:
        break
if b==a:
    print("You guessed the number in %d guesses"%i)
else:
    print("You couldn't guess the number in %d guesses"%i)
