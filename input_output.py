#Q .no 1 
#creat a list of number 1 to 5
num=[1,2,3,4,5]
print(num)

#creat a list of number 1 to 5 
fruits=["apple" , "orange" , "kiwi" ]
print(fruits)

#creat a mixed type of list 
mixed = mixed=[10,20,"car","bus",3.5,4.8]
print(mixed)

#Modify the elements of list by index
num=[1,2,3,4,5]
print(num)
num[2]=8
print(num)

#Append an element to the end
num=[1,2,3,4,5]
print(num)
num.append(6)
print(num)

#Insert an element at a specific index
num=[1,2,3,4,5]
print(num)
num.insert(2,6)
print(num)

#Remove an element by value
fruits=["apple","orange","Kiwi"]
fruits.remove("orange")
print(fruits)

#Remove an element by index
fruits=["apple","orange","Kiwi"]
deleted_element=fruits.pop(1)
print(fruits)
print(deleted_element)

# length of the list
fruits=["apple","orange","Kiwi"]
length=len(fruits)
print(length)

#Check if an element is in a list
fruits=["apple","orange","Kiwi"]
member = "apple" in fruits
not_member = "Mango" in fruits
print("Is 'apple' in the list?\n", member)
print("Is 'Cherry' in the list?\n", not_member)

#display the elements of the list
fruits=["apple","orange","Kiwi"]
for i in fruits:
     print(i)

#Without Using inBuilt Functions like + or extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
newlist = []
for i in list1:
     newlist.append(i)
for i in list2:
    newlist.append(i)
print(newlist)

#Using + Operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
NewList = list1 + list2
print(NewList)

# Using extend()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# Using User-Defined Function
def concat(list1, list2):
    NewList = []
for i in list1:
    NewList.append(i)
for i in list2:
    NewList.append(i)
    "return NewList"
list1 = [1, 2, 3]
list2 = [4, 5, 6]
ResList = concat(list1, list2)
print(ResList)

#using max() and min() built-in function (simple method)
number= [10,20,30,40,50]
max_value = max(number)
min_value = min(number)
print("maximum :", max_value)
print("minimum :", min_value )

#using sorted() function 
number = [10,20,30,40,50]
sorted_number = sorted(number)
max_value = "sorted_nunber"[-1]
min_value = sorted_number[0]
print("maximum:", max_value)
print("minimum:", min_value)

# Using a for Loop (Manual Method)
numbers = [10, 20, 5, 40, 50]
max_value = numbers[0]
min_value = numbers[0]
for num in numbers:
    if num > max_value:
     max_value = num
    if num < min_value:
     min_value = num
print("Maximum:", max_value)
print("Minimum:", min_value)

#Using While loop
numbers = [10, 20, 5, 40, 50]
index = 1 # Start from the second element
max_value = numbers[0]
min_value = numbers[0]
while index < len(numbers):
    if numbers[index] > max_value:
      max_value = numbers[index]
    if numbers[index] < min_value:
     min_value = numbers[index]
    index += 1
print("Maximum:", max_value)
print("Minimum:", min_value) 


