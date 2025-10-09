def func():
    print("function")


if (
    __name__ == "__main__"
):  ## __name__ gives file name, default = main, if using inside file name as 'module':
    print("we're inside the __name__ == __main__")
    func()
