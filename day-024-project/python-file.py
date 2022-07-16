# Python FILE
#! open file and save in a variable
#! mode = r read only, w write only, a append
file = open("D:\Python\MAIN\myfile.txt", mode="a")

#! same as above line of code but it auto closes
# ? with open("D:\Python\MAIN\myfile.txt") as file:

#! write new text
file.write("\nHello World!")

#!close file
file.close()

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")
