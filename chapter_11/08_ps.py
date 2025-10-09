## practise set of chapter 11


## Q-1) create a class with 2d vector to 3d vector
# class twoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"{self.i}i, {self.j}j of twoDVector class ")


# class threeDVector(twoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"{self.i}i, {self.j}j, {self.k}k of threeDVector class ")


# a = twoDVector(1, 2)
# a.show()
# b = threeDVector(1, 2, 3)
# b.show()


## Q-2) create a class pets from class Animals, furthur create class dog from pets and bark method into dog class
# class Animals:
#     pass


# class Pets(Animals):
#     pass


# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bhao Bhao")


# b = Dog()
# b.bark()


## Q-3) write a method salaryAfterIncrement() method with a property decorator with setter which changes the value of increment based on salary
# class Employer:
#     salary = 200
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + self.salary * (self.increment / 100)

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         # self.increment = (salary / self.salary) - 1 * 100
#         self.increment = ((salary / self.salary) - 1) * 100


# e = Employer()
# # print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 400  # gives them salaryafterincrement it will gives you how much percentage increment
# print(e.increment)


## Q-4) write a complex class to add and multiply correctly
# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)

#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imaginary_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imaginary_part)

#     def __str__(self):
#         return f"{self.r} {self.i}i"


# c1 = Complex(3, 4)
# c2 = Complex(5, 6)

# print(c1 + c2)
# print(c1 * c2)


## ##  Q-5) write a function for display 3 dimentions of vector
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result

#     def __str__(self):
#         return f"{self.x}i + {self.y}j + {self.z}k"


# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)

# print(v1 + v2)
# print(v1 * v2)

# print(v1 + v3)
# print(v1 * v3)


## ##  Q-6) write a __len__ function
# class Vector:
#     def __init__(self, l):
#         self.l = l

#     def __len__(self):
#         return len(self.l)


# v1 = Vector([2, 55, 2, 1, 4, 6])
# print(len(v1))
