# Data Structure

tup = (1,'abc',2,'cde')
tup1 = 3,'efg',True
tup2 = 'A '
print(tup[0:2])
try:
    tup[3] = 5
except Exception as e:
    print(e)
print(tup2*4)
print(5 in tup)
for x in ('a', 'b','c'):
    print(x)
def muliple_result():
    return (1,2,'a')
print(muliple_result())