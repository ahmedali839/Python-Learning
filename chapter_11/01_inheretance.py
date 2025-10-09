class College:
    name = "Govrt College"

    def printCollege(self):
        print(f"The name of College is {College.name}")


class Teacher(College):

    def printTeacher(self):
        print(f"The name of Teacher is {Teacher.name}")


a = College()
b = Teacher()

# a.printCollege()  ## error: because we read parent values not child values
b.printCollege()
b.printTeacher()  # takes "name" from parent as inheritance
