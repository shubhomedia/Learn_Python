def Isprime(n):
    for x in range(2, int(n/2+1)):
        if not n % x :
            return False
    return True
def PrimesTo(n):
    for x in range(2,n):
        if Isprime(x):
            print(x)
