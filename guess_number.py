print("Hello everyone welcome to Dice Playing")
chances = 3
import random
import time
random = random.randint(1,6)
for i in range (1, chances+1):
    user = int(input("Enter a number: "))
    if user < random :
        print("You guessed low")
    elif user == random:
        print("You guessed correct")
        time.sleep(1)
        print("You are the winner")
        break
    elif user > random:
        print("You guessed high")
    left_chances = chances - i
    print("Remainig chances are available only: ", left_chances)
    if left_chances == 0:
        print("run out chances")
        break

else:
    print("The numbers should be in 1 To 6 ")
print("Thank you")

