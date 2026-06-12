#classes and objects
class car:
    def car(self, model, year, price,color, mileage):
        self.model = model 
        self.year = year
        self.color = color
        self.price = price
        self.mileage = mileage
    def display(self):
        print(f"Model: {self.model}, Year: {self.year}, Price: {self.price}, Color: {self.color}, Mileage: {self.mileage}")

tesla = car()
tesla.car("Model 3", 2020, 35000, "Red", 15000)
tesla.display()

honda = car()
honda.car("Civic", 2018, 20000, "Blue", 30000)
honda.display() 
 
BMW = car()
BMW.car("X5", 2021, 60000, "Black", 10000)
BMW.display()   

Cevorlet = car()
Cevorlet.car("Camaro", 2019, 40000, "Yellow", 20000)
Cevorlet.display()  


