# simple lambda function

f = lambda a: lambda b: lambda c: a*b*c
print(f(5)(3)(2))
