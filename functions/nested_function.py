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
print(outer(10))

# nested function like loop
def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g

print(f(5)(2)(3))
