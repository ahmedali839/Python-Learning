### chapter 04 practise set:

## Q-1) write a program to store seven fruits in list entered by user
# x = []

# a = input("Enter first fruit: ")
# x.append(a)
# b = input("Enter second fruit: ")
# x.append(b)
# c = input("Enter third fruit: ")
# x.append(c)
# d = input("Enter fourth fruit: ")
# x.append(d)
# e = input("Enter fifth fruit: ")
# x.append(e)
# f = input("Enter sixth fruit: ")
# x.append(f)
# g = input("Enter seventh fruit: ")
# x.append(g)
# print(x) ## show the filled list with user entered fruits

## same question with for lop easily

# for fruit in range(7):
#               a = input("Enter different fruit name: ")
#               x.append(a)

# print(x)    






## Q-2) write a program to take marks of six students and show them in sorted manner:
# y = []
# for marks in range(6):
#         a = input(f"Enter mark of {marks+1} student: ")
#         y.append(a)
#         y.sort()
# print("marks of six students in sorted manner: ", y)



## Q-3) write a program to check that type cannot be changed in python
# a = 10
# b = str(a)
# print(type(b)) ## yes type can change but only int to str not str to integar 




## Q-4) write a program to sum of list 4 numbers
# c = [2,4,10,30,50,20]
# d = (c[0:4]) ## output -> 46
# d = (c[-4:-2])  ## output -> 40
# print(sum(d))



## Q-5) write a program to count the number of zeros in the following tuple: 
z = (0,0,45,2,0,10,50,100)
print(z.count(0)) # count returns the number of value that matches count method value wit tuple


## extra:
# a = (3, 44, "ahmed")
# a[0] = 2 ## we cannot change datatype of tuple, tuple is immutable
