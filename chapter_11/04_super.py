class College:

    def __init__(self):
        print("it's College Constructor.")


class Teacher(College):

    def __init__(self):
        print("it's Teacher Constructor.")

    def insideTeacher(self):
        print("it's inside Teacher function.")


class Student(Teacher):

    def __init__(self):
        super().__init__() # super() means “run the parent’s version of this function.”
        super().insideTeacher()
        print("it's Student Constructor.")


# a = College()
# b = Teacher()
c = Student()
