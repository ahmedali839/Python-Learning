class Maths:
    def __init__(self, num):
        self.n = num

    def __len__(self):
        return 1

    def __add__(self, val):
        return self.n + val.n

    def __mul__(self, val):
        return self.n * val.n

    def __sub__(self, val):
        return self.n - val.n

    def __truediv__(self, val):
        return self.n / val.n


a = Maths(2)
b = Maths(1)

print(len(b))  ## gives the length

print(a * b)
print(a / b)
print(a + b)
print(a - b)
