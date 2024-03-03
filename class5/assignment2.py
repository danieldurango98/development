'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input("Hello, please enter your email address: ")
print(email)

# Clean input
email = email.strip()
print(email)

# Test 1: It has a "." at the third-to-last index
email = 'danieldurango@gmail.com'
test_1 = (email[-4] == '.')

print('Test 1: Does the email have a "." at the third-to-last index?',test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email cannot be @.com
test_2 = ('@' in email[-6::-1])
print('Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email cannot be @.com',test_2)

# Test 3: There is at least one character before the "@" symbol
character_before = email.find('@')
test_3 = (character_before > 0)
print('There is at least one character before the "@" symbol',test_3)

# my_email_index = email.index('d')
# my_email_find = email.find('a')
# print(my_email_index)
# print(my_email_find)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = (' ' not in email)
print('Test 4: It does not have any spaces (does not contain " ")',test_4)

#Final Test with and Keyword
final_test = test_1 and test_2 and test_3 and test_4
print(final_test)