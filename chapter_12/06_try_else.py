try:
    a = int(input("Enter you a number: "))
    print(a)

except Exception as e:  ## error handler for multiple errors
    print(e)

else:  ## else will run when try ran successfully.
    print("I'm running with try.")
