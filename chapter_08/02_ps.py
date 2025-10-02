## ## Practise set of chapter 08

## Q-1) write a program using function to find the greatest number out of three number 
# def Greatest(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(c>a and c>b):
#         return c
#     elif(b>a and b>c):
#         return b
    
# result1 = Greatest(1, 2, 3)
# result2 = Greatest(4, 65, 7)
# result3 = Greatest(997, 998, 999)
# print(result1)
# print(result2)
# print(result3)




## Q-2) write a program using function to convert Celcius to Fahrenhiet
# def Cel_to_Fah(F):
#     C = 5 * (F -32)
#     return C
# a = Cel_to_Fah(50)
# b = Cel_to_Fah(80)
# print(f"The Celcius of {50} is: {a}°C")
# print(f"The Celcius of {80} is: {b}°C")




## Q-3) write a program to prevent to print new line after one line
# print("a without end variable.")
# print("b without end variable.")
# print("c with end variable. ", end="")
# print("d with end variable. both will be on same line.", end="")




## Q-4) write a recrusive function that sum of the first n natural numbers
# def Addition(n):
#     if(n==1):
#         return 1
#     return n + Addition(n-1)

# result = Addition(10)
# print(result)




## Q-5) write a function to print first following n lines of the following patterns:
'''
***
**
*   when n = 3
'''

# def Lines(n):
#     if(n==1):
#         return "*"
#     return "*" * n + "\n" + Lines(n-1)
    
# r1 = Lines(3)
# r2 = Lines(7)
# print(r1)
# print(r2)





## Q-6) write a python function to convert inches into cms
# def inches_to_cms(n):
#     return n * 2.54
# result  = inches_to_cms(4)
# print(f"The centemeters are: {result}")



## Q-7) write a python function to remove a character of element int the list and strip at same time
# l = ["Ahmed", "Ahtesham", "Ahsan", "Qasim"]

# def word_remover(l , word):
#     stripped_list = [item.replace(word, "").strip() for item in l]
#     return stripped_list

# result = word_remover(l, "Ahte")
# print(result)





## Q-87) write a python function to write a table of n number
def writing_table(n):
 for item in range(1, 11):
    print(f"{n} X {item} = {n*item} \n")

writing_table(2)
writing_table(5)
writing_table(10)
