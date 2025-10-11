# def square(n):
#     return n * n

## lambda pattern > func name = lambda props: return
square = (
    lambda x: x * x
)  # lambda mini version of function, writing func in expression form
sum = lambda a, b, c: a + b + c
strr = lambda a, b: f"a is: {a}\nb is: {b}"

print(square(3))
print(sum(1, 2, 3))
print(strr(2, 3))
 