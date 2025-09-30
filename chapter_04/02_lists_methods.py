a = ["ahmed", "Amjad", 5,5 , False, None, "Junaid"]

# lists are mutable so we can change it's original value
a[0] = "akhtar"
# print(a)

# methods: 
a.append("Atif") # append needs direct value to append/add into last of list(array)
# print(a)


b = a.count("ahmed") # count returns number of values that inside of the list same that you asked  
# print(b)


a.insert(2, 33) # inserts ask 1 value as index and 2 value as direct value you want to add
# print(a)


a.remove(5) # remove needs directly value you want to remove inside list, it will delete only first occurence
# print(a)


c = a.index(5) # index returns the exact index of value you entered in index, same value should present inside list
# print(c)

d = a.pop(2) # pop needs index of value you want to delete inside the list
# print(d)


a.copy() # returns the copy (duplicate of list)
# print(a)


e = 5 in a # 'value in list',it returns True or False as dependend on value present in list or not
# print(e)


a.reverse() # reverse arrange value starting from last to first
# print(a)

x  = [2,34,56,2,5,1,0,999]
# x  = [ "qasim","ahmed"]
x.sort() # it arrange the value asc to desc inside the list, it will work with str or int at a time  
# print(x)