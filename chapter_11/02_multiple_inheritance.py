class College:
    name = "Govrt College"

    def printCollege(self):
        print(f"The name of College is {College.name}")


class Teacher(College):
    a = "CSS"

    def printTeacher(self):
        print(f"The name of Teacher has {self.a} value. and parent value is {self.name}")


class Student(Teacher):
    name = "Ahmed"

    def printName(self):
        print(f"The name of Student is {Student.name}")


a = College()
b = Student()

# a.printCollege()  ## error: because we read parent values not child values
b.printCollege()  # print"Ahmed" means self.name inside refers to where it calls from, it calls from Programmer so it takes name = "Ahmed" always
b.printTeacher()
b.printName()
