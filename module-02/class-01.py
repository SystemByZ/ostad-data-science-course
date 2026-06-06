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
a=(0,3,6,5)
b=(10,2,5,2)
if a<b:
    print("b is bigger")
else:
    print("a is bigger")