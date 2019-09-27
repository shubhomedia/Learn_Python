import random

min = int(input("enter the minimum number of the die"))
max = int(input("enter the maximum number of the die"))

N=int(input("enter the number of dice you want to roll?"))
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")

    for i in range(1,N+1):
        print (random.randint(min, max))

    roll_again = input("Roll the dices again?")
    if(roll_again == "yes" or roll_again == "y"):
        N=int(input("enter the number of dice you want to roll?"))
    else:
        print ("bye!!")