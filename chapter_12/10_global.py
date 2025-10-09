a = 1


def val():
    a = 2
    print(a)


print(a)  # output: 1 because we're calling globaly scoop it takes global scoop value
val()  ## output: 2 because we're calling function scoop value it takes function inside value first

