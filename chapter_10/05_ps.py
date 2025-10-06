## practise for chapter 10

## ## Q-1) create a class for storing information of few programmers
# class programmers:
#     Akbar = "Website Developer"
#     Bilal = "QA insuranec"
#     Atif = "Frontend Developer"


# programmer = programmers()
# print(f"Akbar is {programmers.Akbar} , Bilal is {programmers.Bilal} and Atif is {programmers.Atif},")


## ## Q-2) create a class of calculator capable to give square, cube and square root of number
# import math

# class calculator:
#     number = 5

#     def square(self):
#         print(f"Square of {self.number}: ", self.number * self.number)

#     def cube(self):
#         print(f"Cube of {self.number}: ", self.number * self.number * self.number)

#     def square_root(self):
#         print(f"Square root of {self.number}: ", math.sqrt(self.number))


# getSquare = calculator()
# getSquare.square()

# getCube = calculator()
# getCube.cube()

# getSquareRoot = calculator()
# getSquareRoot.number = 25
# getSquareRoot.square_root()


## ## Q-3) create a class make it's new object does new object.variable change the variable of class or not
# class a():
#     name = "Akbar"

# b = a()
# b.name = "Akram"
# print(a.name)
# print(b.name)   ## no, instance cannot the class values, it creates copy of variables if we make changes


## ## Q-4) create a class make it's new object does new object.variable change the variable of class or not
# class a:
#     name = "Akbar"

#     @staticmethod ## static makes it independent of passing "self" inside the function
#     def greet():
#         print("Hello Good Morning.")

# b = a()
# print(
#     b.greet()
# )  ## no, instance cannot the class values, it creates copy of variables if we make chang


## ## Q-5) create a class of train which has methods to book seats, remaining no of seats and fare under Pakistani railways
# class train():
#     seats = 40
#     fare = 20

#     def __init__(self):
#        self.n = int(input("Book number of seats out of 40 ? "))

#     def get_information(self):
#        self.fare = self.fare * self.n
#        self.seats = self.seats - self.n
#        print(f"You booked {self.n} seats so, your total fare is: {self.fare}. And remaining seats are {self.seats}")

# form = train()
# form.get_information()


## ## Q-6) can you change the self-parameter inside the class to say something else "Ahmed" or "Hello World" to see the effects
class a:
    name = "Ahmed"

    def changing_parameter(self):
        self = (
            self.name
        )  ## if we change the self-parameter it takes the value of it's right hand side variable
        print("Change self-parameter inside class to see effects: ", self)


b = a()
b.changing_parameter()
