#hierarchical inherit

class Student:
    def student(self):
        self.name = "John"
        self.roll = 2

    def display(self):
        print(f"Name = {self.name}, Roll = {self.roll}")

x= Student()
x.student()
x.display()        