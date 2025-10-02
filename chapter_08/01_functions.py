## functions executes the number of statement for specific role a

# def Additiosn(a, b, c):
#     d = sum([a,b,c])
#     return print(d)

# Additiosn(1,3 ,3)
# Additiosn(1,4 ,6)
# Additiosn(1,1 ,1)



## ## another function
# def Greeting(name, greet):
#     print(f"{name}, Good {greet}!")

# Greeting("Ahmed","morning")
# Greeting("Ahmed","night")


## ## function recursion
## write a function for factorial
'''
5! -> 1
      1 X 2
      1 X 2 X 3 
      1 X 2 X 3 X 4
      1 X 2 X 3 X 4 X 5

      multiply(n) : n * (n-1) 1 * 2 * 3 * 4 ..... n

 recursion => multiply(n) : n * factorial(n-1)     
'''
# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     val = n * factorial(n-1)
#     return val

# n = int(input("Enter a number for factorial: "))
# val = factorial(n)
# print(val)