try:
    a = int(input("Enter you number: "))

except ValueError as e:  ## error handler for when user enter unexpected or wrong value
    print("Invalid Value", e)

except Exception as e:  ## error handler for multiple errors
    print(e)
