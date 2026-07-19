import keyword

print("===================================")
print(" Welcome to Student Information ")
print("===================================")

# Variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

# String
course = "Python Programming"

# Concatenation
print("\nHello " + name + "!")

# Type Conversion
next_age = age + 1

print("Next year you will be", next_age)

# Sum of Two Numbers
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print("Sum =", total)

# Keywords
print("\nTotal Python Keywords:", len(keyword.kwlist))
print(keyword.kwlist)

print("\nCourse:", course)

print("\nThank you for using this project!")
