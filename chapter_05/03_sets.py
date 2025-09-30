## set() mean well-defined collection of values.
## empty set() -> e = set(). not -> e = {} 

a = { 1, 3, 6, 33, 88, 10000 ,999.9, 99 }
b = { 1, 2, 6, 55, 9.8 , 99 }
c = {1, 3}

# print(a, type(a)) # give you all values of a set
# print(a.union(b)) # give you union mean the collecting values of two sets, don't repeate same values.
# print(a.intersection(b)) # give you interaction mean the common values between two sets
# print(a.add(5)) # add the value into existing set to random index.
# print(a.difference(b)) # it differentiate values from first given set to second given set
# print(a.difference_update(b)) # gives the differentiate from b
print(a.issuperset(c)) # return Boolean, issuperset mean 'a' set's elements includes the all 'c' set's element
print(c.issubset(a)) # return True when all items in 'c' set present in 'a' set
print()