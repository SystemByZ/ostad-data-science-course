# print("hello world")

# x=10
# print(type(x))

# y='hello'
# print (type(y))

# print ("enter your name: ")
# name = input()
# print("nice to meet you,",name)
# age=input("enter your age: ")
# print("you are",age,"years old")
# print("you are " + age + " years old")

# num_int=10
# num_float=10.5
# num_new=int(num_int+num_float)
# print("the value of num_new is:", num_new)
# print("the datatype of num_int is:", type(num_int))
# print("the datatype of num_float is:", type(num_float))
# print("the datatype of num_new is:", type(num_new))

# new_int=27
# new_str="456"
# new_sum=str(new_int)+new_str
# print(new_sum)
# print("type of new_int is:", type(new_int))
# print("type of new_str is:", type(new_str))
# print("type of new_sum is:", type(new_sum))

# a=True
# b=False
# print("the value of a is:", a)
# print("the value of b is:", b)
# print("the type of a is:", type(a))
# print("the type of b is:", type(b))

a=5
b=2
# temp=a
# a=b
# b=temp
a,b=b,a

# print("the value of a is:", a)
# print("the value of b is:", b)

# x="hello"
# print(x[0:3])

n=input("enter a number between 0 and 100: ")
n=int(n)
if n<=100 and n>=90:
    print("grade A")
elif n<90 and n>=80:
    print("grade B")
elif n<80 and n>=70:
    print("grade C")
elif n<70 and n>=60:
    print("grade D")
elif n<60 and n>=50:
    print("grade E")
elif n<50 and n>=40:
    print("grade E-")
elif n<40 and n>=0:
    print("grade F")
else:
    print("invalid input")