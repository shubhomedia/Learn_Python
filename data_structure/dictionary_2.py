# my dictionary file shallow copy

my_dictionary = {'Item':'Shirt','Size':'Medium','Price':50}
my_dictionary1 = my_dictionary

print(my_dictionary)
my_dictionary['Size']='Small'
print(my_dictionary1)


