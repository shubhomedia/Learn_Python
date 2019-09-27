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

'''
# output
enter the minimum number of the die1
enter the maximum number of the die5
enter the number of dice you want to roll?2
Rolling the dices...
The values are....
5
1
Roll the dices again?y
enter the number of dice you want to roll?
'''