import re

intro = print('Hi, here are some requirements you must abide by. The username must start with a lowercase letter and only contain letters, numbers, and underscores. The password must be at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces.')

taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']

error_messages = ['Invalid Username', 'Username Taken', 'Invalid Password', 'Username and Password do not match']

while True:
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    failed_conditions = []

    # Does not contain taken usernames
    if username in taken_usernames:
        failed_conditions.append(error_messages[1])
    
    # lowercase test
    if not username[0].islower() or not username.isidentifier():
        failed_conditions.append(error_messages[0])

    # Password Requirements
    # Must be 8 characters long
    if len(password) < 8:
        failed_conditions.append(error_messages[2])

    # Contains one uppercase and one lowercase
    if not any(u.isupper() for u in password) or not any(u.islower() for u in password):
        failed_conditions.append(error_messages[2])

    # Contains at least one digit
    if not re.search(r'\d', password):
        failed_conditions.append(error_messages[2])

    # Contains at least one special character
    if not re.search(r'[!@#$%^&*()_+-=]', password):
        failed_conditions.append(error_messages[2])

    # Doesn't contain any spaces
    if ' ' in password:
        failed_conditions.append(error_messages[2])

    # If any conditions failed, print the error messages and continue the loop
    if failed_conditions:
        for message in failed_conditions:
            print(message)
        continue

    # Check if username and password match
    username_again = input('Please enter your username again: ')
    password_again = input('Please enter your password again: ')

    # Check if entered username and password match from initial input
    if username == username_again and password == password_again:
        print("Registration Successful!")
        break
    else:
        print(error_messages[3])  # Username and password do not match, restart loop
