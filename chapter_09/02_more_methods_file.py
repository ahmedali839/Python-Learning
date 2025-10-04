'''
we are working with real files inside computer storage
'''

f = open("fileNames.txt", "w+") # "w" method create file and if already exists so, overwite it whole data automatically 
a = open("fileNames.txt", "a") # "a" method use to append mean to add new values at end of data inside other file
a.write("hey, I'm writing something into other.") # 'write' method only work for empty files, use "a" with opening file for adding data into existed data in the file
a.close()
f.close()




# with open("file.txt", "a") as newFile: ## with keyword autoclose the file, with "with" keyword we don't need to do "file.close()"
#     newFile.write("\nHey, I'm appending something here right ?")




# with open("file.txt") as newFile: ## with keyword autoclose the file, with "with" keyword we don't need to do "file.close()"
#     print(newFile.read())
### we don't need to explicity to close the file.




## ## readline method:
f = open("file.txt") 
line1 = f.readline() ## readline() auto read lines one-by-one in order form automatically.
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

line4 = f.readline()
print(line4)