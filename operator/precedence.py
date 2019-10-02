# Python works with this precendence

"""
    1st : ()
    2nd : **
    3rd : *
    4th : /
    5th : %
    6th : +
    7th : -
"""
print(25*15*32/2.0)
a = 25*15
b = 33/2.0
print(a+b)

print((25 * 15 + 33)/2.0)
a = 25 * 15 + 33
b = 2.0
print(a/b)

#Simple Line Break
print("\n")

print((5.0 * (8+(16-2.0/(4+1))/2)) % 4)
a = 16 - 2.0
b = 4+ 1
c = a /b
e = 8 + c
f = e / 2
g = 5.0 * f
h = g % 4
print(h)