 #string
name = input("Enter your name : ")
#integer
age = int(input("enter your age : "))
#float
marks =  float(input("enter your marks : "))
#complex number 
c = complex(input("enter a complex number (example : 2+3j): "))
#boolean 
student = input("Are you a student ? (true/false): ")
student = (student == "true")
#list 
list_values = input("enter list value separated by spaces :  ")
my_list = list_values.split()
#tuple 
tuple_value = input("enter tuple value separated by space : ")
my_tuple=tuple_value . split()
my_tuple = tuple(my_tuple)

print("\n--- entered value ---")
print("name : ",  name )
print(type(name))
print("age :" ,age )
print("marks:", marks )
print(type(marks))
print("complex number:", c)
print(type (c))
print("boolent:", student)
print(type(student))
print("list:", my_list)
print(type(my_tuple))
print("tuple :", my_tuple)
