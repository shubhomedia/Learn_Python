import random
hidden = random.randrange(1,20)
print(hidden)
hidden = random.randrange(1,20)
guess = int(input("Please Enter your Guess:"))

if guess == hidden:
    print("Hit!!")
else:
    print("Wrong!!")