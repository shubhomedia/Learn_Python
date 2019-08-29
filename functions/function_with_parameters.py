#function with arguments
def parameters(a):
    print(a)

parameters("This is input parameter") # a = this is input value pass on the function

#add function using parameter
def add(x,y,z):
    sum = x + y + z
    return sum

new_result = add(10,20,30)
print(new_result)

#function with default value
def addv2(z,x=10,y=20):
    sum = x + y + z
    return sum

result = addv2(10) # only z value passed
print(result)

#scope example
def scope(a):
    a = a + 1
    print(a)
    return a

scope(10)
print(a) # a is not define because a only work on in the function