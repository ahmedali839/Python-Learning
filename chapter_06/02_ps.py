## Practise set of chapter 06

# ## Q-1) show the one greatest number out of four numbers entered by user
# a1 = int(input("Enter nunmber 1st: "))
# a2 = int(input("Enter nunmber second: "))
# a3 = int(input("Enter nunmber third: "))
# a4 = int(input("Enter nunmber fourth: "))

# if(a1>a2 and a1>a4 and a1>a3):
#     print(f"Greatest number is {a1}")

# elif(a2>a1 and a2>a4 and a2>a3):
#     print(f"Greatest number is {a2}")

# elif(a3>a1 and a3>a2 and a3>a4):
#     print(f"Greatest number is {a3}")
# else:
#     print(f"Greatest number is {a4}")




# ## Q-2) show the student passed or failed depend on condition and student should have total percentage  more than 40 and 33 percenteage indiviually in subjects
# a1 = int(input("Enter marks 1st: "))
# a2 = int(input("Enter marks second: "))
# a3 = int(input("Enter marks third: "))

# total_percentage = (100 * (a1+ a2+ a3))/300

# if(total_percentage > 40 and a1>=33 and a2>=33) and a3>=33:
#     print("You're passed.", total_percentage)

# else:
#     print("You failed.", total_percentage)




## Q-3) write a program to detect spam text if containing one of the keywords: 'click now', 'buy now' and 'otp'
# spam_words = ["click now", "buy now", "otp"]
# a3 = input("Enter your text: ")

# if(a3 in spam_words):
#     print("Spam text detected.")
# else:
#     print("Clear text.")




## Q-4) write a program find username contain 10 characters or not
# a1 = input("Enter a username: ")

# if(len(a1)<=10):
#     print("Enter username has less than 10 characters: ", len(a1))

# else:
#     print("Enter username has more than 10 characters: ", len(a1))





## Q-5) write a program find given username whether present in list or not
# names_list = ["Akhtar", "Ali", "Amjad"]
# a1 = input("Enter your username: ")

# if(a1 in names_list):
#     print("Entered name already in the list: ", a1)

# else:
#     print("Entered name not in the list: ", a1)





## Q-6) write a program to figure the grade of  marks dependent on the marks 
# mark  = int(input("Enter your mark: "))

# if(mark>=90 and mark<=100):
#     print("Grade A")

# elif(mark>=80 and mark<=90):
#     print("Grade B")

# elif(mark>=70 and mark<=80):
#     print("Grade C")

# elif(mark>=60 and mark<=70):
#     print("Grade D")

# elif(mark>=50 and mark<=60):
#     print("Grade E")

# else:
#     print("Grade F mean failed.")







## Q-7) write a program to figure out the post talking about harry or not in python ? 
post = input("Enter your full post: ")
name = "Harry"

if(name in post):
    print("Yes, it talking about Harry.")

else:
    print("No, it's not about Harry.")