## Q-1) write a program that user enters a number then display it in English dictionary:
words = {
    "paani": "water",
    "roti": "bread",
    "amrood": "guaava"
}
# word = input("Enter you favourite word one of following: 'paani','roti' and 'amrood': ")
# print(words[word])


## Q-2) write a program that user enters 8 numbers then display all numbers as unique (at once)
# e = set() ## we use set because set take well-defined and unique values
# for number in range(7):
#     n = input(f"Enter number {number+1}th: ")
#     e.add(n)
# print(e)    



## Q-3) Can we have a set having values int(18) and "18" at a same time.
# e = {
#     18,
#     "18"
# }
# print(e) ## -> return: 18, '18' because dataType unique


## Q-4) what will be length of set if: 
# e = set()
# e.add(18),
# e.add("18"),
# e.add(18.0) ## length ? 
# print(len(e)) ## -> length will be 2, How? 1. is '18' and 2. is 18 once it accepts the integer set will ignore float N otherwise accepts only float, but one at a  time



## Q-5) what type of s = {} 
# s = {} # will be dict. "s = set() -> set"
# print(type(s))



## Q-6) create empty dict, allow 4 friends to add their fav foods as values of dict and their names as key of dict
# names = ["Ahmed", "Akbar", "Amjad"]
# d = {}

# for items in names:
#     e = input(f"{items} Enter your favourite language: ")
#     d[items] = e ## working fine
#     # d.update({f"{items}":f"{e}"}) ## working but it's special for updating
# print(d)





## Q-7) create empty dict, allow 4 friends to add their fav foods as values of dict and their names as key of dict, assume that friends names are unique
# count = 0
# d = {}

# for items in range(4):
# while count < 4:
#     name = input(f"Enter your Name initially: ")

#     if name in d.keys():
#         print(f"Error: given {name} already in use, Enter your different name: ")
#         continue

#     language = input(f"{name} your favourite language: ")

#     d[name] = language
#     count += 1
# print(d)







## Q-8) create empty dict, allow 4 friends to add their fav languages as values of dict and their names as key of dict, assume that friends names are unique and languages are unique
# count = 0
# d = {}

# for items in range(4):
# while count < 4:
#     name = input(f"Enter your Name initially: ")

#     if name in d.keys():
#         print(f"Error: given {name} already in use, Enter your different name: ")
#         continue

#     language = input(f"{name} your favourite language: ")

#     if language in d.values():
#         print(f"{language} language is already used, choose another language")
#         continue

#     d[name] = language
#     count += 1
# print(d)





## Q-9) Can we change the values inside in list inside set() in python
y = set()
# y.add(["akbar", "ahmed", "ali"]) # -> no we cannot. return error because set() are mutable(changeable) but they cannot contain any immutable(not changeable) inside of it. 
y.add("akbar") # we can add one well-defined element at a time into set().

print(y)