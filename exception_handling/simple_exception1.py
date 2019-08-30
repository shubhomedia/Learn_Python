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

# raise function

a = 1
def RaiseException(a):
    if type(a) !=type('a'):
        raise ValueError("This is not string")
try:
    RaiseException(a)
except ValueError as e:
    print(e)

#test case

def TestCase(a,b):
    assert a<b, "a is greater than b"
try:
    TestCase(2,1)
except AssertionError as e:
    print(e)