#Print Built in Function

# greeting = 'Happy Wednesday'
# print(greeting)


# first_name = 'Daniel'
# print(first_name)

# Addition

# print(4 + 2)
# print(5 + 5)
# print(100 + 5)

# Subtraction

# print(10 - 3)
# print(4 - 3)
# print(10 - 5)    
      
# Multiplication

# print(3 * 3)
# print(2 * 8)
# print(5 *7)

# Division

# print(10 / 2)
# print(5 / 3)
# print(5 / 0)

# try:
#     print(5 / 0)
# except ZeroDivisionError as e:
#     print("You cannot divide by zero, have a great day!")    

# Exponents
# print(5 ** 5)
# print(2 ** 5)
# print(3 ** 6)

# Integer Division
# print(10 // 3)
# print(4 // 3)
# print(5 // 2)

# Modulo/Mod/Remainder
# print(5 % 2)
# print(10 % 4)
# print(6 % 2)

# Program to find the perimeter of a rectangle

#  perimeter = 2 * (lengh + width)

# length = 10
# width = 7

# perimeter = 2 * (length + width)
# print('The perimeter of this rectangle is', perimeter)


# Data Types


# Integer
# num_one = 5
# print(num_one)
# print(type(num_one))

# String
# fav_color = 'blue'
# print(fav_color)
# print(type(fav_color))


# Bool
# technical_errors = True
# print(technical_errors)
# print(type(technical_errors))

# Float
# num_two = 1.22
# print(num_two)
# print(type(num_two))

# String
# first_name = 'Daniel'
# last_name = 'Durango'
# fullname = first_name + ' ' + last_name
# print(fullname)
# print(first_name, last_name)

# List 
# student_grades = [100 , 95, 70, 85, 40]
# print(student_grades)
# print(type(student_grades))

# For loop
# for s in student_grades:
#     print(s)

# Dictionary
# demographic_info = {"First Name": "Daniel",
#                     "Last Name": "Durango",
#                     "State": "New York"}
# print(demographic_info)
# print(type(demographic_info))

# Cast a string to an integer
# my_string = '5'
# print(type(my_string))
# new_number = int(my_string) # casting our string to an integer
# print(new_number)
# print(type(new_number))

# Cast integer to string
# second_num = 10
# print(type(second_num))

# new_string = str(second_num)
# print(new_string)
# print(type(new_string))

# Colors
# fav_colors = ['blue', 'green', 'red', 'brown'] # List item has 4 elements
# num_colors = len(fav_colors)
# print(num_colors)

# color = 'orange'

# my_count = len(color)
# print(my_count)
# print(type(my_count))

# for c in color:
#     print(c)


# Fahrenheit to Celsius
# fahrenheit = 89
# celsius = (fahrenheit - 32) * 5/9
# print(celsius)


# # Eval
# cold_weather = 'True'
# print(eval(cold_weather))

'''
# You are given a triangle with a side #1 of 4, base of 6, and side #2 of 3. Create
a brief python script that will determine the perimeter of the triangle. Comment your code

1. Print the perimeter
2. Using boolean operators is side #1 greater than the base?
3. Using boolean operators is side #2 less than the base?
4. Using boolean operators is base larger than or equal to side #1?
'''

# Perimeter of a Triangle
# perimeter = side_one + base + side_two

# Variables

side_one = 4
base = 6
side_two = 7

# Formula
perimeter = side_one + base + side_two
print(perimeter)
print('Using boolean operators is side #1 greater than the base?',side_one > base)
print('Using boolean operators is side #2 less than the base?',side_two < base)
print('Using boolean operators is base larger than or equal to side #1?',base >= side_one)



