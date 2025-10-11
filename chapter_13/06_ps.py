## practise set chapter 13
from functools import reduce

## ## Q-1) write a program to print student statement with format function
# name = input("Enter name: ")
# marks = input("Enter marks: ")
# phone = input("Enter phone number: ")


# a = "The name of the student is {0}, his marks are {1} marks, his phone number is {2}".format(
#     name, marks, phone
# )

# print(a)


## ## Q-2) write a program to convert table into string
# table = [str(7 * i) for i in range(1, 11)]
# s = "\n".join(table)
# print(s)


## ## Q-3) create a list of numbers only divisible by 5
# n = [4, 3, 22, 5, 10, 55, 95, 10000]

# def divisible(n):
#     if n % 5 == 0:
#         return n
#     return False

# print(list(filter(divisible, n)))




## ## Q-4) find the maximum number from a list
# n = [223, 3, 22, 5, 10, 55, 95, 10000]

# def greatest(a, b):
#     if a > b:
#         return a
#     return b

# print(reduce(greatest, n))



## ## Q- 5) find the maximum number from a list
