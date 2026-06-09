# Topic:List, Tuple, Set, Dictionary



# this_list = ["apple", "banana", "cherry"]
# print(this_list)
# # print(this_list[1])
# # print(this_list[-1])
# # print(this_list[2:5])
# print(this_list[:4])
# # print(this_list[2:])   
# print(this_list[-1:-4:-1])    

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list3)
# list4 = ['abc', 34, True, 40, "male"]
# print(list4)

# list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(list1)
# print(list1+["tomato", "grape",140])
# print(list1, ["tomato", "grape",140])
# print(list1*4)
# print(list1[2])
# print(list1[-1:-8:-1])
# print(fruits)
# fruits.insert(1, "lemon")
# print(fruits)
# fruits.remove("banana")
# print(fruits)
# fruits.clear()
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.count("cherry")
# x=fruits.count("cherry")
# print(x)
# fruits.extend(["grape", "melon", "mango"])
# print(fruits)
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.index("cherry")
# x=fruits.index("cherry")
# y=fruits.index("cherry", x+1)
# z=fruits.index("cherry", y+1)
# print(x)
# print(y)
# print(z)
# print(fruits)
# fruits.remove("cherry")
# fruits.remove("cherry")
# fruits.remove("cherry")
# print(fruits)
# print(len(fruits))

# A=[[1,2,3,4],[4,5,6,7],[4,7,8,9]]
# print(A)
# print(A[0])
# print(A[1])
# print(A[2])     
# print(A[0][0])
# print(A[0][1])
# print(A[0][2])
# print(A[0][3])
# print(A[1][0],end=" ") 
# print(A[1][1],end=" ")
# print(A[1][2],end=" ")
# print(A[1][3])   
# print(A[2][0],end=" ")
# print(A[2][1],end=" ")
# print(A[2][2],end=" ")
# print(A[2][3])   

# column = [[2],[5],[7]]
# for row in A:
#     column.insert(0,row[1])
# print(column)


# tuples start here

# this_tuple = ("apple", "banana", "cherry")
# print(this_tuple)

# fruits = ("apple", "banana", "cherry")
# print(fruits)
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

#For loop practice

# sum=0
# for i in range(0,101):
#     if i%2==0:
#         sum=sum+i
# print(sum)
# this_list = ["apple", "banana", "cherry"]

# for fruits in this_list:
#     print(fruits )
#     for i in fruits:
        
#         if i=="r":
#             continue
#         print(i ,end="")
#         print(" ")

# print("This is the end of the program")


# n=int(input("Enter a number:",))
# if n % 2 != 0:
#     print("Weird")
# elif (n%2==0 and 1<n<6):
#     print("Not Weird")
# elif (n%2==0 and 5<n<21):
#     print("Weird")
# elif (n%2==0 and 20<n):
#     print("Not Weird")

# A=[[1,2,3,4],[4,5,6,7],[4,7,8,9]]
# print(A)
# print("end")
# column=[]
# for row in A:
#     column.append(row[1])
# print(column)
# for i in column:
#     print([i])

# for i in column:
#     for j in A:
#         if i in j:
#             print(j)

#Tuples start here
# this_tuple = ("apple","banana","cherry")
# print(this_tuple)

# fruits = ("apple", "banana", "cherry")
# print(fruits)
# (red,green,yellow)=fruits
# print(green)
# print(yellow)
# print(red)
# fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits)
# (red,green,*blue)=fruits
# print(red)
# print(green)
# print(blue)#*blue is used to store the remaining values in the tuple after assigning the first two values to red and green. In this case, blue will contain the values "cherry", "orange", "kiwi", "melon", and "mango".it represents a list of the remaining values in the tuple after the first two values have been assigned to red and green.
# a=(5,6)
# b=(8,4)
# if a>b:
#     print("a is bigger")
# else: 
#     print("b is bigger")

# A=[(5,6),(8,4),(7,9)]
# B=sorted(A)
# print(B)
# a=(0,3,6,5)
# b=(10,2,5,2)
# if a<b:
#     print("b is bigger")
# else:
#     print("a is bigger")


#Set start here

# my_set = {"apple","banana","cherry"}
# print(my_set)
# my_set.add("orange")
# print(my_set)
# my_set.update(["grape","melon","mango"])
# print(my_set)
# # my_set.remove("banana")
# # print(my_set)
# my_set.discard("banana")
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update(["grape","melon","mango"])
# print(my_set)
# for i in my_set:
#     print(i)


# Mixed elements in set
# my_set ={"apple",3.14,True,False,'banana',(1,2,3),(1,2,4)} # this will give an error because set cannot contain mutable elements like list and dictionary
# print(my_set)
# print(type(my_set))


# my_set ={1,2,3,4,5,2,3,4}
# print(my_set) # this will print {1,2,3,4,5}

# a = [1,2,3,4,5,8,9,1,2,3,4]
# b=set(a)
# print(b)

# num1 = {1,2,3,4,5}
# num2 = {4,5,6,7,8}

# print(num1.union(num2)) # this will print {1,2,3,4,5,6,7,8}
# print(num1.intersection(num2)) # this will print {4,5}
# print(num1.difference(num2)) # this will print {1,2,3}
# print(num1.symmetric_difference(num2)) # this will print {1,2,3,6,7,8}
# print(num1.isdisjoint(num2)) # this will print False because num1 and num2 have common elements
# print(num1.issubset(num2)) # this will print False because num1 is not a subset of num2
# print(num1.issuperset(num2)) # this will print False because num1 is not a superset of num2
# print("end ")
# num3 = num1 & num2
# print(num3) # this will print {4,5}
# num4 = num1 | num2
# print(num4) # this will print {1,2,3,4,5,6,7,8}
# num5 = num1 - num2
# print(num5) # this will print {1,2,3}
# num6 = num1 ^ num2
# print(num6) # this will print {1,2,3,6,7,8}

# this_sort= {5,2,9,1,3}
# print(sorted(this_sort)) # this will print [1,2,3,5,9] because sorted() function returns a sorted list of the elements in the set

#dictionary start here

# this_dict = {
#     "company" : "Ford",
#     "Model" : "Mustang",
#     "Year" : 1964,
#     "Color" : "Red"
# }
# print(this_dict)

# this_dict = {
#     "company" : "Ford",
#     "Model" : "Mustang",
#     "Year" : 1964,
#     "Color" : "Red"
# }
# print(this_dict.keys()) # this will print dict_keys(['company', 'Model', 'Year', 'Color'])
# print(this_dict.values()) # this will print dict_values(['Ford', 'Mustang', 1964, 'Red'])
# print(this_dict.items()) # this will print dict_items([('company', 'Ford'), ('Model', 'Mustang'), ('Year', 1964), ('
# print(this_dict["Year"],this_dict["Model"],this_dict["Color"]) # this will print 1964 Mustang Red
# print(this_dict.get("Year")) # this will print 1964
# this_dict["Year"] = 2020 # this will update the value of Year to 2020
# print(this_dict) # this will print {'company': 'Ford', 'Model': 'Mustang', 'Year': 2020, 'Color': 'Red'}
# this_dict["Engine"] = "V8" # this will add a new key-value pair to the dictionary           
# print(this_dict) # this will print {'company': 'Ford', 'Model': 'Mustang', 'Year': 2020, 'Color': 'Red', 'Engine': 'V8'}
# this_dict.pop("Color") # this will remove the key-value pair with key "Color"
# print(this_dict) # this will print {'company': 'Ford', 'Model': 'Mustang', 'Year': 2020, 'Engine': 'V8'}
# this_dict.clear() # this will remove all the key-value pairs from the dictionary
# print(this_dict) # this will print {}                   
# this_dict.update({"company":"Tesla","Model":"Model S","Year":2020,"Color":"Black"}) # this will update the dictionary with the new key-value pairs
# print(this_dict) # this will print {'company': 'Tesla', 'Model': 'Model
# this_dict2 = this_dict.copy() # this will create a copy of the dictionary
# print(this_dict2) # this will print {'company': 'Tesla', 'Model': '
# print(this_dict.get("Year"))

# for i in this_dict.keys():
#     print(i)
# for i in this_dict.values():
#     print(i)
# for i in this_dict.items():
#     print(i)
# for i,j in this_dict.items():
#     print(i,":",j)

#from posixpath import split
#

text = "The banana is common fruit of Bangladesh. It is grown in all the districts and all the seasons. Munsigonj and Narsingdi are famous for banana . banana has several varieties such as Sagore, Shabri, Chapa, Agniswar etc. It is very nutritious and sweet.Papaw is a delicious fruit.It keeps the liver function active. The papaw is grown in all the districts and in all seasons. The coconut is a common fruit of Bangladesh. It grows in all seasons. Its water is a sweet drink and its kernel is a tasty food. The mango , the orange , the lichi , the black-berry , the jack fruits, the pineapple etc. grow in different seasons."
fruits = ["banana", "Papaw", "coconut", "black-berry", "pineapple", "lichi", "orange", "mango"]
# for i in fruits:
#     if i in text:
#         print(i)

text=text.split()
# print(text)
# print("  end  ")
# fullfruits=[]

# for i in fruits:
#     if i in text:
#         fullfruits.append(i)
# print("fullfruits:", fullfruits)

# fruits_set=set({})
# for i in text:
#     if i in fruits:
#         fruits_set.add(i)
# print("fruits_set:", fruits_set)

# fruits_dict={}
# for i in text:
#     if i in fruits:
#         if i in fruits_dict:
#             fruits_dict[i]=fruits_dict[i]+1
#         else:
#             fruits_dict[i]=1
# print("fruits_dict:", fruits_dict)


#hour to minute conversion by using function

# def function(hour):
#     return float(hour)*60

# x=float(input("Enter the time in hour:",))
# print("The time in minute is:", function(x))

# List = [1, 5, 2, 9, 3, 22, 13]

# def function(List):
#     return sorted(List)
# print("The sorted list is:", function(List))

# this_list1= [1,5,6,5,1,2,3]
# this_list2= this_list1.copy()
# print("the duplicate list of this_list1 is :",this_list2)
a = int(input("Enter the first number:",))
b = int(input("Enter the second number:",))
if 1<a<10**10 and 1<b<10**10:
        addition =a+b
        difference =a-b
        product = a*b
    
    
print(addition)
print(difference)
print(product)