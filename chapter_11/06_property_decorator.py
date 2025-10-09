# class Principle:
#     a = 1

#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]


# e = Principle()

# e.name = "Ahmed Yar"
# print(e.fname)
# print(e.lname)


## example:
class Company:

    @property  ## property mean getter
    def data(self):
        print(f"{self.name}\n {self.gender}\n {self.id}\n {self.salary}\n")

    @data.setter
    def EmployerInfo(self, value):
        self.name = value.split(" ")[0]
        self.gender = value.split(" ")[1]
        self.id = value.split(" ")[2]
        self.salary = value.split(" ")[3]


a = Company()
a.EmployerInfo = "Ahmed male 14 10"
print(a.name)
print(a.gender)
print(a.id)
print(a.salary)
