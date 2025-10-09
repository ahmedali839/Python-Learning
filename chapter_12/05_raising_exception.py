try:
    a = int(input("Enter you a number: "))
    b = int(input("Enter you b number: "))
    if b == 0:
        raise ZeroDivisionError("Zero error, zero cannot be divide by any number.")

    print(a / b)

except Exception as e:  ## error handler for multiple errors
    print("Exception multiple errors", e)
    print(e)
