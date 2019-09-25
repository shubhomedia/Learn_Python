name = ['shubho','jamal','kamal']
print(name)
# add new elment
name.append('rony')
print(name)
name.remove('jamal')
print(name)
for x in name:
    print(x)

print("\n")

cars = ["Volvo", "BMW", "Ford", "Mazda"]
for x in cars:
    print(x)

for x in cars:
    if(x == "Ford"):
        break
    print(x)
