# #classes and objects
# class car:
#     def car(self, model, year, price,color, mileage):
#         self.model = model 
#         self.year = year
#         self.color = color
#         self.price = price
#         self.mileage = mileage
#     def display(self):
#         print(f"Model: {self.model}, Year: {self.year}, Price: {self.price}, Color: {self.color}, Mileage: {self.mileage}")

# tesla = car()
# tesla.car("Model 3", 2020, 35000, "Red", 15000)
# tesla.display()

# honda = car()
# honda.car("Civic", 2018, 20000, "Blue", 30000)
# honda.display() 
 
# BMW = car()
# BMW.car("X5", 2021, 60000, "Black", 10000)
# BMW.display()   

# Cevorlet = car()
# Cevorlet.car("Camaro", 2019, 40000, "Yellow", 20000)
# Cevorlet.display()  

# class student:

#     def set_value(self, name, age, grade, roll):
#         self.name =name 
#         self.age = age
#         self.grade = grade 
#         self.roll = roll

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Roll: {self.roll}")

# xihad= student()
# xihad.set_value("xihad", 20, "A", 101)
# xihad.display()

# ismail = student()
# ismail.set_value("ismail", 21, "A+", 103)
# ismail.display()    

# ruku= student()
# ruku.set_value("ruku", 19, "B", 102)
# ruku.display()

# Sorpi = student()
# Sorpi.set_value("Sorpi", 18, "B+", 104)
# Sorpi.display()

# class employee:

#     def __init__(self,department):
#         self.department = department

#     def employee(self, name, salary, position):
#         self.name = name 
#         self.salary = salary
#         self.position = position    

#     def display(self):
#         print(f"Name:{self.name}, Salary: {self.salary}, Department: {self.department}, Position: {self.position}")

# kamal = employee("IT")
# kamal.employee("Kamal", 50000, "Software Engineer")
# kamal.display()

# jamal = employee("HR")
# jamal.employee("Jamal", 40000, "HR Manager")
# jamal.display()

# bo = employee("Finance")
# bo.employee("Bo", 45000, "Financial Analyst")
# bo.display()
 
# fang = employee("Marketing")
# fang.employee("Fang", 55000, "Marketing Manager")       
# fang.display()

# class student:

#     def __init__(self):
#         self.section = "A"

#     def display(self):
#         print(f"Section: {self.section}")

# kamal = student()
# kamal.display()

# class person:
#     pass

# class father:

#     def info(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# kabir = father()
# kabir.info("Kabir", 50)
# kabir.display()


# class son(father):
#     pass


# xihad = son()
# xihad.info("Xihad", 20)
# xihad.display()

class person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def show(self):
        print("This is person1 class")

class person2(person1):
    def show2(self):
        print("This is person2 class")

zihad =person2("Xihad", 20)
zihad.show2()
zihad.show()
zihad.display()