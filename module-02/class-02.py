#functions start here

def add(a,b):
    x = a + b
    return x
def sub(a,b):
    x = a - b
    return x
def mul(a,b):
    x = a * b
    return x
def div(a,b):
    x = a / b
    return x        
x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
print("Addition: ",add(x,y))
print("Subtraction: ",sub(x,y))
print("Multiplication: ",mul(x,y))
print("Division: ",div(x,y))    