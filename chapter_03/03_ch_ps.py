### Exercise of Chapter 03

## Q-1) write a program to display user entered name followed by "Good Afternoon", without contacinating
# name = input("Enter your name: " )
# print(f"Good Afternoon, {name} " )

## Q-2) write a program to fill with letter template/value of given <|Name|> and <|Date|>
a = '''
Dear  <|Name|>, you are selected at Google <|Date|>
'''
# print(a.replace("<|Name|>", "Ahmed").replace("<|Date|>", "Today"))



## Q-3) write a program to detecet double spacing in a string
a = "Ahmed is  a   boy"
# print(a.find("   ")) # find and give index of first value matched within data


##Q-4) write a program to replace "" to '' in string
a = "Ahmed is  a  boy"
# print(a.replace("  ", ' ')) # replace the given value to matched value that already exists in string



##Q-5) write a program to format the string below with escape sequence characters
a = "Hey, \n\t Ahmed how are you ? \n Thanks"
print(a)
