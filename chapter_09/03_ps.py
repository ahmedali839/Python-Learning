## ## practise set of chapter 09

# ## Q-1) write a program to read 'poem_ps.txt' and check it has or not the word 'terrible'
# l = []
# word = "terrible"

# with open("poem_ps.txt") as f:
#         data = f.read()
#         if word in data:
#             print("Yes, terrible was found in poem_ps.txt file.")
#         else:
# print("Yes, terrible was not found in poem_ps.txt file.")


# ## Q-2) write a program to for game function, let the user play a game, and you need to read a file which blank or contains the previous HI-score, you need to update that score whenever game function breaks the HI-score

# def game(n):
#      with open("GAME-HI-SCORE.txt", "r") as f:
#         data = f.read()
#         i = int(data)  if data else 0 ## here if file empty start with 0
#         print(f"You choosed {n}")
#         if(n > i):
#             with open("GAME-HI-SCORE.txt", "w") as g:
#                 g.write(str(n))
#                 print(f"New Highest score is: {n}")
#         else:
#             print(f"Highest score was: {data}")

# n = int(input("Choose a number: "))

# game(n)


## ## Q-3) write a program to generate multiplication from 2 to 20 and write into different file inside 'file' folder

# def generate_multiplication():
#     for i in range(2, 21):
#         with open(f"file/{i}_table_file.txt", "w") as f:
#             print("new table")
#             for item in range(1, 11):
#                 value = (f"\n{i} X {item} = {i*item}")
#                 f.write(value)
#                 print(value)

# generate_multiplication()


## ## Q-4)A file contain word "Donkey" multiple times. write a program to update "Donkey" with "######" in the same Line.
# def Donkey_replace(word):
#     with open("poem_ps.txt") as f:
#         data = f.read()
#         new_Data = data.replace("Donkey", "######")
#         if word in data:
#             r = data.count(word)
#             if r > 1:
#                 with open("poem_ps.txt", "w") as g:
#                     # data.replace("Donkey", "######")
#                     g.write(new_Data)
#                     print(f"{word} is replaced, it's done.")
#             else:
#                 print(f"{word} not multiple times.")
#         else:
#             print(f"{word} not found inside file.")

# Donkey_replace("Donkey")


## ## Q-5) repeat the above question but concerned with list instead of one word
## word you want to change should be more than one time in file.

# def word_replace(list_blacklisted):
#     with open("poem_ps.txt", "r") as f:
#         data = f.read()
#         new_Data = data
#         for item in list_blacklisted:
#             if item in new_Data:
#                 r = new_Data.count(item)
#                 new_Data = new_Data.replace(item, "######")
#                 if r > 1:
#                     with open("poem_ps.txt", "w") as g:
#                         g.write(new_Data)
#                         print(f"{list_blacklisted} is replaced, it's done.")
#                 else:
#                     print(f"{list_blacklisted} not multiple times.")
#         else:
#             print(f"{list_blacklisted} not found inside file.")

# n = input(
#     "Enter blacklisted words, that you want to replace with ######, separate each word with ',':  "
# )
# list_blacklisted = [word.strip() for word in n.split(",")]

# word_replace(list_blacklisted)


## ## Q-6) write a program to mine a log file to check whether it contains or not the word 'python'

# def word_checker(word):
#     with open("poem_ps.txt", "r") as f:
#         data = f.read()
#         new_Data = data
#         if word in new_Data:
#             count = new_Data.count(word)
#             if count:
#                 print(f"{word} found {count} times, it's done.")
#             else:
#                 print(f"{word} not found.")
# word = "python"

# word_checker(word)


## ## Q-7) write a program to find on which line python is written in file, with above question.

# found_lines = []

# def word_checker(word):
#     with open("poem_ps.txt", "r") as f:
#         for line_number, line_text in enumerate(f, 1):
#             print(line_number)
#             print(line_text)
#             if word in line_text:
#                 found_lines.append(line_number)
#     if found_lines:
#         print(f"{word} found {len(found_lines)} times.")
#         for i in found_lines:
#             print(f"{word} found on line number {i}.")
#     else:
#         print(f"{word} not found.")

# word = "python"
# word_checker(word)


## ## Q-8) write a program that make a copy of file: "this.txt"

# def create_file_copy():
#     with open("fileNames.txt") as f:
#         data = f.read()
#         with open("poem_ps(01).txt", "w") as g:
#             g.write(data)
#             print("File copy created Successfully.")

# create_file_copy()


## ## Q-9) write a program to identical and matches the whether the  contect of another file or not

# def create_file_copy():
#     with open("fileNames.txt") as f, open("poem_ps(01).txt") as g:
#          for file_lines, (f_line, g_lines) in enumerate(zip(f, g), 1):
#                   if f_line != g_lines:
#                     print(f"File not matched, on the line number: {file_lines}")
#                     print(f" -> in fileNames.txt, the line mismatched: {f_line}")
#                     print(f" -> in poem_ps(01).txt, the line mismatched: {g_lines}")
#                     return # finish the function here

#          print(f"File matched, both have same data.")

# create_file_copy()


## ## Q-10) write a program to wipe out the content of a file using python

# def wipe_whole_content():
#     with open("poem_ps(01).txt", "w") as f:
#         print("poem_ps(01).txt file's content wiped out successfully.")

# wipe_whole_content()


# ## ## Q-11) write a program to rename a file with "renamed.txt"
# import os
# def rename_file_name():
#     # with open("fileNames.txt") as f:
#         # previousName = f.name
#         os.rename("renamed.txt", "fileNames.txt")
#         print("file renamed")

# rename_file_name()
