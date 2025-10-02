'''
file module we use to create, read, write files in our computer storage to store data permanently  
'''

# for reading the data exist in external file we are opening or calling as below: 
a = open("file.txt")
data = a.read()
print(data)
a.close() # it's recommended not essential, because to inform computer we completed our work with this file to avoid useless executation of this file in future.