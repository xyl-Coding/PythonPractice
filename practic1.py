from math import *

name = "Xiangyang Liu"
print(name + " is very cool")
print(name.lower())
print(name.upper())
print(name.isupper())
print(name.upper().isupper())
print(len(name))
print(name[0])
print(name[6])
print(name.index("y"))
print(name.index("Liu"))
print(name.replace("Xiangyang", "Olivia"))

# Working with numbers
print(6 + 6.09 * 12)
print(10 % 3)
my_num = -5
# to print a number next to a string, you have to use srt() function
print(str(my_num) + " is my favority number")
print(abs(my_num))
print(pow(2, 3))
print(max(8, 0))
print(round(9.678697))
print(floor(67.8796))
print(ceil(67.76896))
print(sqrt(49))

# Getting input from user
input("waht is your name")
# print("Hello" + input("what is your name"))
print(len("Xiangyang Liu"))

a = input("a : ")
b = input("b : ")

c = a
a = b
b = c

#a small program
print("Hello There")

city = input("Please tell me the city that you grew up\n")

pet = input(" What is the name of your pet\n")

print("your band name could be " + city + " " + pet) 
