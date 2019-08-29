# simple function code from sololearn

def myfunc():
    print("Spam")
    print("Spam")
    print("Spam")

#call the function
myfunc()

# double number

def print_double(x):
    print(2 * x)

print_double(10) # result = 20

# even or odd .
def even(x):
    if x%2 == 0:
        print("Yes")
    else:
        print("No")

even(5)

# max number
def max(x,y):
    if x>=y:
        return x
    else:
        return y

print(max(4,7))
z = max(8,5)
print(z)