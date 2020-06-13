file_load = open('mbox.txt')
count = 0
for line_count in file_load:
    count = count + 1
print("Line Count: ", count)

whole_file_read = file_load.read()
print(len(whole_file_read))
