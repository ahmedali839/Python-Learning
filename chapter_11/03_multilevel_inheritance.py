class College:
    name = "Govrt College"

    def printCollege(self):
        print(f"The name of College is {College.name}")


class Teacher:
    name1 = "CSS"

    def printTeacher(self):
        print(f"The name of Teacher has {Teacher.name1} value.")


class Student(College, Teacher):
    # name = "Ahmed"

    def printName(self):
        print(f"The name from College: {College.name}. And Teacher: {Teacher.name1}")


a = College()
b = Student()

b.printName() ## it takes the values from it's two parent classes at a time, it's called multilevel inheritance. 
