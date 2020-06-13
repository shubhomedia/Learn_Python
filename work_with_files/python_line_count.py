file_load = open('mbox.txt')
count = 0
for line_count in file_load:
    count = count + 1
print("Line Count: ", count)

read_short_file = open('mbox-short.txt')
x = read_short_file.read()
print(len(x))