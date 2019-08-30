#simple exception handling
try:
    a = 5/0
except Exception as e:
    print(e)

# value error

try:
    n = int(input("Enter your integer:"))
    print(n)
except ValueError:
    print("That is not a integer")