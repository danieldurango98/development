''' Loops and conditionals '''

'''
What is the difference between a For and While Loop?
How do I write a For Loop?
How do I write a While Loop?

'''
# For Loop
colors = ['green', 'blue', 'orange', 'yellow']

# for c in colors:
#     print(c)

# While Loop
''' initialization of variables'''

limit = 26  
start = 0

# while start < limit:
#     print(start) # feedback for the user
#     start += 1


''' Break Keyword '''

# Lets look at the 2 examples below and take note where the loop stops

south, north, west, east = 10, 5, 6, 11 # initializating variables on one line

# south = 10
north = 5
west = 6
east = 11

print(south, north, west, east)

userin = '' # initialization of variable

# while userin != 'stop':
#     userin = input('Enter something or hit stop to leave the loop ')
#     print(userin)

# while True:
#     userin = input('Enter something or hit stop to leave the loop ')
#     if userin == 'stop':
#         break
#     print(userin)

''' Break in nested loops '''



'''
Exercise

Write some code that takes in numbers from a user one at a time. This should keep going until the user enters 0. Then print the sum of all the numbers.
If the user inputs something that isn't a number, an error message should appear and the program should stop. (Hint: use break)

Example (no error):
5
12
0
Sum: 17

Example (error):
5
7
c
Error: Not a number

'''
'''Declare any needed variables'''




''' Continue keyword '''

''' Example
Use the continue keyword to loop through a string and only print the vowels.
'''
# Option 1


# Option 2



''' 
Exercise:
Sum of Even Digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''




''' Break, Continue, and Pass '''




'''
Exercise

Write some code that takes in strings from a user one at a time.
After each string is taken in evaluate if the string is empty, a number, a set of letters, or contains symbols.
If the string is empty, stop the loop.
If the string is a number, convert it to a float and add it to a total.
If the string is a set of letters, concatenate to the other letter strings passed in.
If it contains a symbol, or is none of the above, do nothing and repeat the loop.
Make sure to use break and/or continue.


REQUIREMENTS
    If the string is empty, stop the loop.
    If the string is a number, convert it to a float and add it to a total.
    If the string is a set of letters, concatenate to the other letter strings passed in.
    If it contains a symbol, or is none of the above, do nothing and repeat the loop.


'''


'''These variables will be placeholders for the total and new string we will be creating'''


