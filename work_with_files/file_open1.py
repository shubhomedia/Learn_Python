# simple file open
file =  open("E:\\MY_DATA\\Data Science\\Learn_Python\\work_with_files\\file.txt","r")
print(file.read())
print(file.read(4)) # input 4 bytes
file.close() # close the file

# loop
file =  open("E:\\MY_DATA\\Data Science\\Learn_Python\\work_with_files\\file.txt","r")
for line in file:
    print(line)
file.close() # close the file