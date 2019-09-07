# oop sample 1
class Complex:
    'this class simulates complex numbers'
    def __init__(self, real = 0,imag = 0):
        if(type(real)not in(int,float)) or type(imag) not in (int,float):
            raise Exception('Args  are not Number')
        self.real = real
        self.img = imag
    def getReal(self):
        return self.real
    def getImag(self):
        return self.img
try:
    c = complex(2,4)
    print(c.real,c.imag)

except Exception as e:
    print(e)


