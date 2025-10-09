def main():
    try:
        a = int(input("Enter you a number: "))
        print(a)

    except Exception as e:  ## error handler for multiple errors
        print(e)

    finally:  ## finally will always run does'nt matter function in try or except, finally always run
        print("I'm running in finally, because i'm in finally.")


main()
