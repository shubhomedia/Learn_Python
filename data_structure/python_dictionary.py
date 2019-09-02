#python Dictionary
my_dictionary = {'key':'value',('K','E','Y'):5}
my_dictionary1 = {x:x+1 for x in range(10)}
print(my_dictionary['key'])
print(my_dictionary1)

try:
    print(my_dictionary[1])
except Exception as e:
    print(e)
