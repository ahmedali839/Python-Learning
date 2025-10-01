# if, elif and else are conditional rendering statements which runs when it's own condition comes True. 
# '    ' is before rendering statment is called indent

a = int(input("Enter your age: "))

if(a>18):
    print("You're Eligible to drive a car.")

elif(a>70):
       print("You're Illegible, because of too old to drive a car.")

elif(a<=0):
       print("You're Illegible, because of invalid age.")

elif(a<18):
       print("You're Illegible, because of too young to drive a car.")

else:
      print("Invalid Age.")