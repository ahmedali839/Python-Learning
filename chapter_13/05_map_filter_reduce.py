from functools import reduce

# Map Example
names = ["Ahmed", "Akhtar", "AbdulHadi", "Atif"]
num = [3, 21, 11, 1, 98, 68]

# s = map(lambda x: x.upper(), names)
# print(list(s))

# FIlter Example
# def even(n):
#     if n % 2 == 0:
#         return True
#     return False


# onlyEven = filter(even, num)
# print(list(onlyEven))


# Reduce Example
def sum(x, y):
    return x + y


mul = lambda x, y: x * y


print(reduce(sum, num))
print(reduce(mul, num))
