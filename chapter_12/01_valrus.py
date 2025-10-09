listss = [2, 43, 66, 7, 11, 99, 0, 999, 100]
if (
    a := len(listss) > 4
):  ## walrus := means to chek two conditions at a time, like here checking what's length of list and is this greater than 4 ?
    print(f"List have length {a} more length {4} ")
else:
    print(f"List have length less than {4}")
