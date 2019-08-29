#nested function
def add(x,y,z): # simple function
    sum = x + y + z
    return sum

#nested function
def outer(a):
    def nested(b):
        return b * a;
    a = nested(a)
    return a

