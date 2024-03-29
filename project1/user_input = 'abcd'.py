import re

user_input = 'abcd'
# contains_num = any()


contains_num = re.search(r'\d', user_input) # will look for a digit in the string
if contains_num:
    print(f'Test Passed: {user_input} contains a number')
else:
    print(f'Test Failed: {user_input} does not contain a number')
