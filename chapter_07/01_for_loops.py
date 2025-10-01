## for loops used to run repetition of program, it make easy to iteration instead of writing indiviusally

list_names = ["ahmed","ali", "akbar", False, 2, 33, 999, "Amjad"]
list_int = [2, 55, 77, 33, 666, 342, 10, 1]


# for i in range(5):
#     print(i)
   


# # print(len(list_names))

# for i in range(len(list_names)):
#     print(list_names[i])



for i in range(len(list_int)):   # for loop with else, else will run after for loop completed
    print(list_int[i])
    
else:
    print("for loop done.") # else with for loop run when for loop exhausted    
