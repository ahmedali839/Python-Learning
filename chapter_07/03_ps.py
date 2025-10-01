### practise set of chapter 07 of for, while and for-else loop

## Q-1) write a program to generate table of given number with for loop
# n = int(input("Enter the number to get it's table: "))

# for i in range(11):
#     print(n*i)



# ## Q-2) write a program to get all person names in list that starts with S
# list_names = [ "Sham", "Shamshad", "Ali", "Qasim", "Shahzeb"]

# for i in list_names:
#     if i.startswith("S"):
#         print(i)




## Q-3) write a program to generate table of given number with while loop
# n = int(input("Enter the number to get it's table: "))
# i = 1

# while(i < 11):
#     print(i*n)
#     i += 1





## Q-4) write a program to whether it's prime number or not
# n = int(input("Enter to check prime or not: "))

# if (n%2 == 0) and (n%3 == 0):
#     print("it's Prime Number")

# else:
#     print("it's not a Prime Number")



## Q-5) write a program to sum of n natural numbers of using while loop
# n = int(input("Enter you number: "))
# list_num = []
# i = 1

# while(i < n+1):
#     print(i)
#     list_num.append(i)
#     i += 1
# print(sum(list_num))





## Q-6) write a program to write factorial of given number using for loop
# n = int(input("Enter you number: "))
# list_num = 1

# for i in range(1, n+1):
#     list_num = list_num * i

# print("The factorial is ", list_num)





## Q-7) write a program to print star of number of star:
# n = int(input("Enter you number: "))

# for i in range(n+1):
#     print("*" * i )
#     print("\n")

   




## Q-8) write a program to print star of number:
# '''
#   *
#  *** 
# *****  
# '''
# n = int(input("Enter you number: "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
    # print("")











## Q-9) write a program to print star of number of star:
# '''
#        * * *
#        *   *
#        * * *
# '''

n = int(input("Enter you number: "))

for i in range(1, n+1):
    if(i==1 or i==n):
        print("*" *n, end="")
    else:
        print("*", end="")
        print(" "* (n-2) , end="")
        print("*", end="")
    print()        







   
## Q-10) write a for loop that prints table of n number but in reverse order
# n = int(input("Enter a number, I'll give a table of it: "))

# for i in range(10, 0, -1):
#     print(f"{n} * {i} = {n*i}")

