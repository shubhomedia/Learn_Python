# simple lambda function

f = lambda a: lambda b: lambda c: a*b*c
print(f(5)(3)(2))

# lambda function 2
f = lambda c: lambda a,b : lambda d:(c*(a+b)) % d

print(f(2)(4,3)(11))