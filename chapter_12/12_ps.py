## ## practise set chapter 12

### Q-1) write a program to open 3 files 1.txt, 2.txt, 3.txt if any of the file not present display the error message without crashing the program
# try:
#     with open("1.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("2.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("3.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)


### Q-2) write a program to print 3rd, 5fth, 7th number from a list using enumerate
# lists = [3, 2, 66, 33, 9, 1, 11, 44, 666, 34, 66]

# for index, value in enumerate(lists):
#     if index == 3 or index == 5 or index == 7:
#         print(value)


### Q-3) write a list compresention that print the table of multiplication of that number user entered
# n = int(input("Enter a number: "))
# list_data = []

# for value in range(1, 11):
#     list_data.append(value*n)

# print(list_data)


### Q-4) write a to print a/b where b=0 show zeroDivisionError:
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# if b == 0:
#     raise ZeroDivisionError("0 cannot be divide by any integer")
# print(a / b)


### Q-5) store the table of n to print a/b where b=0 show zeroDivisionError:
n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]

with open("table.txt", "a") as f:
        f.write(f"Table of {n}: {str(table)} \n")
