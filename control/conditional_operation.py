#This file for Conditional Statement like if then that.

nameinput = input("Enter your name: ")
print("welcome to Learn Python",nameinput)

question1 = input("what is your name ?\n")
if question1 == nameinput:
    print("Thanks Acceptable:")
elif question1 == "Other":
    print("Wrong Information,but go on")
else:
    print("Wrong Answer")