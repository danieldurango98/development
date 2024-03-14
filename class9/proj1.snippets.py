import re


''' What are some of the things we may come across while building this project'''

'''Initialization and prompt (and testing)'''

# first_input, second_input = '', ''

# while True:
#     first_input = input("Please enter your data ")
#     second_input = input("Please enter your data ")

#     print(first_input, second_input)
#     break

'''Handling error messages with a list (and testing)'''

error_message = ['Error message 1', 'Error message 2', 'Error message 3']

# if 5 > 7:
#     print(error_message[0])
# else:
#     print(error_message[2])


'''Testing a string'''

# Example of string testing (testing for lowercase letter)
# test_string = 'Popeye1989'

# # Testing for uppercase as first letter
# first_letter = test_string[0]
# lower_case_test = first_letter.islower()

# if lower_case_test:
#     print('This string failed lowercase testing')
# else:
#     print('This string passed lowercase testing')


''' Taken usernames '''
# sample_word = 'blue'
# sample_list = ['green', 'blue', 'orange', 'yellow', 'purple']

# if sample_word in sample_list:
#     print('Word exist in the list')
# else:
#     print('Word does not exist in list')


''' Using Break and Continue to control the flow of loop'''

# If input is a number we will go through this while loop and continue through, if not, we will send the user back to the beginning

# while True:
#     userinput = input('What is your test string? ')

#     if userinput.isnumeric():
#         print('This is a number, we will stay in the loop')
#     else:
#         print('Not a number, have the user try again')
#         continue
#     print('if you see this line of code, we are still in the loop')
#     break

''' Password requirements '''

test_string = 'C1234567'
# At least 8 characters long

# Contains at least one uppercase letter
one_uppercase = False
for t in test_string:
    if t.isupper():
        one_uppercase = True

# print('Contains at least one uppercase letter?', one_uppercase)

# Even better, is the any function! Tests if any of items in iterable is true
# any_uppercase = any(u.isupper() for u in test_string)
# print('Contains at least one uppercase letter?', any_uppercase)

# Or Regular Expressions match method

# uppercase_test_regex = bool(re.match(r'\w*[A-Z]\w*', test_string))
# print('Contains at least one uppercase letter?', uppercase_test_regex)

''' Logging in and handling the loop'''

# These can represent the user id and password the user created
sys_username = 'simonsays123'
sys_password = 'fido1950'


# These can represent the re-authentication
username = 'simonsays123'
password = 'fido1950'

# Lets check for a match

# while True:

#     if sys_username == username and sys_password == password:
#         print('Login Successful')
#         break
#     else:
#         print('Incorrect username and password')