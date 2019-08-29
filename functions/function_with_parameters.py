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
