# simple recursive function

def factorial(n):
    if n == 1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5)) # 120 output

#simple recurtion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
