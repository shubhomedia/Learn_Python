# oop sample 1
class Complex:
    'this class simulates complex numbers'
    def __init__(self,real,imag):
        self.real = real
        self.img = imag
try:
    c = complex(1,1)
except Exception as e:
    print(e)
print(c.real,c.imag)
