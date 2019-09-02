# simple sets file
my_set = set(['one','two','three','one'])
my_set1 = set(['two','three','four'])
print(my_set1 | my_set) # union of set
print(my_set1 ^ my_set) # inter section of set
print(my_set1 - my_set) # Different

a = my_set - my_set1
print(a <= my_set)