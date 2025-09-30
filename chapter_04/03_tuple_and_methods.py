a = ("ahmed", "Amjad", 5,5 , False, None, "Junaid") # tuple are immutable like string which we cannot be change it's original value, it always create copy of tuple before work with tuple

## tuple are immutable so we cannot change it's original value

# methods: 
# print(type(a)) ## returns the data type of any variables value


b = a.count(5) # it returns the number of same values inside tuple as same as you entered inside count
# print(b)


c = tuple(reversed(a)) # first have to mention attribute type like 'tuple' then inside method call the reversed() function then give tuple attribute name like 'a' in parenthesis -> "tuple(reversed(a))"
print(c)