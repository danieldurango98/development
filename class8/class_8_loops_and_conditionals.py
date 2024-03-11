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

# south, north, west, east = 10, 5, 6, 11 # initializating variables on one line

# south = 10
# north = 5
# west = 6
# east = 11

# print(south, north, west, east)

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
# i = 3
# while i > 0:
#     print(i)
#     i -= 1
#     if i == 4:
#         break
# else:
#     print('done')


userin = ''
# taking a string from the user until they hit stop
# while userin != 'stop':
#     userin = input("Please enter a word or hit stop to end the loop ")

#     for l in userin: # looping through the input from the user
#         if l.isalpha(): # we are testing to see if each character is in the alphabet
#             print(l)
#         else:
#             break
#     print("This is our next line")



# while True:
#     userinput = input("Please enter your word ")
#     print("we are on line 78")
#     print(userinput)
#     print("we are still in the while loop")
#     break
#     print("I will not print, because we used the break keyword above me")

# print("Why am I printed??") # this is outside the loop



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

# userinput, sum = '', 0


'''Start our loop'''
# while True:

#     userinput = input("Please enter your number: ")
#     print(userinput)
# test for a letter
    # if userinput.isalpha():
    #     print("Error: Not a number")
    #     break

# convert to integer, end and print sum if zero, otherwise continue to add to sum
    # userinput = int(userinput) # recast to integer
    # if userinput == 0:
    #     print(f'Sum: {sum}')
    #     break
    # else:
    #     sum += userinput
        

'''Get our input'''


'''Test for letter'''


'''Convert to integer, end and print sum if zero, otherwise continue to add to sum'''



''' Continue keyword '''

''' Example
Use the continue keyword to loop through a string and only print the vowels.
'''
# Option 1 # this method can be used to look for taken usernames
# test_string = 'hello'
# vowels = 'aeiou'                          # this can be used for taken usernames
# vowels = ['a', 'e', 'i', 'o', 'u']    

# for t in test_string:
#     if t in vowels:
#         print(t)
#     else:
#         continue

# Option 2

# for t in test_string:
#     if t in 'aeiou':
#         print(t)
#     else:
#         continue


''' 
Exercise:
Sum of Even Digits

Take a string as user input, and verify that it's a number.
Loop through each digit of the number, and only add it to the sum if it's even.
Print the sum of all the even digits at the end. 
Make sure to use the continue keyword.
'''
# .isdigit

# user_input, sum = '', 0

# while True:
#     user_input = input("Please enter your string: ")
#     for u in user_input: # loop through the string entered by the user
#         if u.isalpha():
#             continue # continue will allow us to skip the letters
#         else:
#             u = int(u) # recasting to a number
#             if (u % 2) == 0:
#                 sum += u
#     print(sum)

''' Break, Continue, and Pass '''
word = 'hello'
vowels = 'aeiou'

# for l in vowels:
#     if l in vowels:
#         print(l)
#         break

# for l in word:
#     if l in vowels:
#         continue
#     print(l)

# for l in word:
#     if l in vowels:
#         pass
#     print(1)


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

new_total = 0
new_string = ''

while True:
    user_input = input("Please enter your data: ")

    # if empty stop the loop
    if len(user_input) == 0:
        print('String is empty, stopping the loop')
        break
