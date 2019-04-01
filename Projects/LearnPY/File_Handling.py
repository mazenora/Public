# try:
#     file1 = open("abc.txt", "a")
#     file1.write("Hello")
#     file1.close()
# except Exception as e:
#     print("Error while writing the file ",e)
# else:
#     print("Writing Done...")

# try:
#     file1 = open("abc.txt","r")
#     print(file1.read())
#     file1.close()
# except Exception as e:
#     print("Read Error", e)
#
# print(file1.closed) #True or False if file is closed


# with open("abc.txt") as myfile:
#     print(myfile.read())
#
# print(myfile.closed)

# courses = ["Java", "Python", "C#", "C++"]
# with open("abc.txt","w") as f1:
#     f1.writelines(courses)
# help(f1.write)

# with open("abc.txt","r") as f1:
#     #print(f1.read(10)) #10 char
#     #print(f1.readline(3)) #3 char from first line
#     for line in f1.readlines():
#         print(line)

# with open("abc.txt","r") as f1:
#     print(f1.tell()) # reading position
#     f1.seek(10,0) # move reading position 10 char from beginning
#     print(f1.read())
#     print(f1.tell())
# with open("abc.txt","r+") as f1:
#     print(f1.tell()) # reading position
#     f1.write("Start File")
#     f1.seek(0,2) # move reading position to the end
#     f1.write("End File")
#     print(f1.tell())
import os
print(os.path.isfile("abc.txt"))