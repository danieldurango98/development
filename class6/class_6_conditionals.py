''' Conditionals '''

''' Lets follow through the two code snippets below'''

# This will run
x = 20
y = 15

# if x > y:
#     print(x)

# This will not run
x = 20
y = 20

# if x > y:
#     print(x)



'''
Exercise

Write some code that prints “This is odd” if the user inputs an odd number.
(Hint: use an if statement)
Example:
User input: 7
This is odd
'''
# user_input = int(input('Please enter your number'))

# if user_input % 2 != 0:
#     print ('This is odd')

# We can use modulus to figure out odd or even
# val = 7
# result = val % 2
# print(result)


'''Exercise Solution'''



''' Else If (Elif) Statements '''
'''
We want a small program that will tell a student their grade based on the following scale

A - Between 90 and 100
B - Between 80 and 89
C - Between 70 and 79
D - Between 65 and 69
F - Anything under 65
'''
# Get grade from user
# score = int(input('Please enter your grade: ' ))

# Creat our conditional
# Option 1
# if score >= 90 and score <= 100:
#     print('Grade A')
# elif score >= 80 and score < 90:
#     print('Grade B')
# elif score >= 70 and score < 80:
#     print('Grade C')
# elif score >= 65 and score < 69:
#     print('Grade D')
# else:
#     print('Grade F')

# Option 2
# if 90 <= score <= 100:
#     print('Grade A')
# elif 80 <= score < 90:
#     print('Grade B')
# elif 70 <= score < 80:
#     print('Grade C')
# elif 65 <= score < 69:
#     print('Grade D')
# else:
#     print('Grade F')

# Option 3
# if score >= 90:
#     print('Grade A')
# elif score >= 80:
#     print('Grade B')
# elif score >= 70:
#     print('Grade C')
# elif score >= 65:
#     print('Grade D')
# else:
#     print('Grade F')




'''
Exercise
Add to your previous code so it prints “This is odd” if the user enters an odd number, and “This is even” if the user enters an even number.
(Hint: add an elif statement)

Examples:
User input: 7
This is odd

User input: 12
This is even

'''

''' Exercise solution with an elif and else'''

# user_input = int(input('Please enter your number '))

# With an elif
# if user_input % 2 != 0:
#     print ('This is odd')
# elif user_input % 2 == 0:
#     print('This is even')



# # With an else statement
# if user_input % 2 != 0:
#     print ('This is odd')
# else:
#     print('This is even')


'''
Exercise
Add to your previous code so if the user enters something that isn't an odd number or an even number, print “Unknown”.


Examples:
User input: 7
This is odd

User input: 12
This is even

User input: 9.2
Unknown


'''

''' Exercise solution(s)'''


# Check if it is a decimal

# user_input = input('Please enter your number: ')


# try:
#     user_input = int(input('Please enter your number: '))
# except:
#     print('Unknown')
# else:
#     if user_input % 2 != 0:
#         print('This is odd')
#     else:
#         print('This is even')




'''
Exercise

Write some code that takes in a string from the user and prints whether the string is a number, if it is a word, or something else.

Examples:
User input: 7
This is a number
String method - isdigit

User input: abcde
This is a word
String method - isalpha

User input: 7!ab5
This is something else

'''
# user_input = input('Please enter your data: ')

# if user_input.isdigit():
#     print(f'{user_input} is a number')
# elif user_input.isalpha():
#     print(f'{user_input} is a word')
# else:
#     print(f'{user_input} is something else.')



'''Chaining Conditionals code results'''

# Mutually exclusive
    
# temp_f = 35
# if temp_f > 70:
#     print("It is hot outside")
# elif temp_f > 40:
#     print("It's moderate outside")
# else:
#     print("It's cold outside")


# result - evaluated separately and multiple of them could be run
    
# temp_f = 75
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside")

# 70 won't run
# temp_f = 70
# if temp_f > 70:
#     print("It is hot outside")
# if temp_f > 40 and temp_f < 70:
#     print("It's moderate outside")
# if temp_f <=40:
#     print("It's cold outside")


# nested conditionals
# num = 5

# if num % 2 == 1:
#     if num < 10:
#         if num > 0:
#             print("This is a single digit odd number")

# if num % 2 and num < 10 and num > 0:
#     print("This is a single digit odd number")


'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''



# Prompt the user to enter their username and password using the input() function. use strip() as well 
username = input('Hello, please enter your username: ')
# print(username)
password = input('Please enter your password: ')
# print(password)
# Create two variables called username and password and set them to any valid string values.

username = username.strip()
password = password.strip()

username = 'durango'
password = 'cancode123'

# Create your conditional, includes your conditional

if username == username:
    print('Login successful')
elif username != username:
    print('Incorrect username or password')

if password == password:
    print('Login successful')
elif password != password:
    print('Incorrect username or password')


