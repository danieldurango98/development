''' Class 4 Strings '''

# String operators

'''Concatenation'''
# operator_code = 'A987'
# part_id = "49Be"
# print(operator_code + part_id)
# item_number = operator_code + part_id
# print(item_number)


''' Create two variables, one to capture first name, another for last name. Combine them to a third variable to display the user's full name. '''
# first_name = 'Daniel'
# last_name = 'Durango'
# full_name = first_name + ' ' + last_name
# print(full_name)


''' Multiplication '''
greeting = 'hip hip hooray ' * 3
print(greeting)

''' Using multiplication, create a new string that multiplies your favorite color 5 times'''

color = 'blue ' * 5
print(color)

# Reference vs Value equality
x = 'hello'
str2 = 'HELLO'.lower()



''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''
test_character = 'b'
test_string = 'bananas'


''' create a quick test to see if the sub string 'spreh' can be found in the string 'Incomprehensibilities' '''
test_chars = 'spreh'
test_word = 'Incomprehensibilities'



''' len() - Returns the length of a string, aka the number of characters in a string.'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'


''' create a variable that holds a string of your favorite animal, create a variable to capture the length of that animal's string value'''
animal = 'zebra'


# String methods

word_1 = 'happy' # capitalize me!


ex_1 = 'cereal' # capitalize me!


word_2 = 'SuPrISe' # make me lower case!


ex_2 = 'RuMMaGe' # make me lower case!


word_3 = 'ZOO' # make me lower case!


ex_3 = 'PLANET' # make me lower case!

'''FUN FACT: Whereas casefold() method is an advanced version of lower() method, it converts the uppercase letter to lowercase including some special characters which are not specified in the ASCII table for example ‘ß’ which is a German letter and its lowercase letter is 'ss'.
'''

word_4 = 'Good Evening'


ex_4 = 'Hello World!' # center me within a space of 65 characters


word_5 = 'Pseudopseudohypoparathyroidism' # How many p's?


ex_5 = 'Antidisestablishmentarianism' # how many times does the letter 'e' occur?


word_6 ='I\tam\ta\ttab'

ex_6 = "Let's\t do\t some\t coding!" # lets try to increase the tabs to 10 whitespaces

# Find the position of the letter k
word_7 = 'Omphaloskepsis'

ex_7 = 'Dichlorodifluoromethane' # find the position of the letter f

word_8 = 'Supercalifragilisticexpialidocious'


'''Fun Fact - Both index() and find() are identical in that they return the index position of the first occurrence of the substring from the main string. The main difference is that Python find() produces -1 as output if it is unable to find the substring, whereas index() throws a ValueError exception.'''


# isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z and 0-9

test_1 = 'abcdef'
test_2 = '%$123'


ex_8 = '123*' # Am I alphanumeric?

# isalpha() Are all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345'

ex_9 = 'LMN0P' # Are we all in the alphabet

# isdecimal() Are all characters decimals?

test_5 = '1234P'
test_6 = '234567'


ex_11 = '123456' # Check for decimals?

# isdigit() Are all characters digits?

test_7 = 'H1234'
test_8 = '9876'


ex_10 = '123Hello' # Check for digits!

''' Fun fact isdecimal() method supports only Decimal Numbers. isdigit() method supports Decimals, Subscripts, Superscripts. 
isnumeric will check for unicode characters
'''


# islower() Lets check for lowercase

test_9 = 'Zebra'
test_10 = 'affordable'


ex_12 = 'Username' # check if all lowercase

# isupper() lets check for ALL uppercase

test_11 = 'Marshall'
test_12 = 'HALLOWEEN'


ex_13 = 'TEMPLE' # check if uppercase

# isspace() Lets check for whitespace (someone enters nothing for an input)

test_13 = '    '
test_14 = 'j      b    c'


ex_14 = '   ' # check if whitespace


# istitle() Let's check for title case

test_15 = 'Eye of the tiger'
test_16 = 'Eye Of The Tiger'


ex_15 = 'Tempus Fugit' # check for title casing

# join() Joins the elements of an iterable to the end of the string

my_colors = ['blue', 'green', 'red', 'orange', 'blue']


ex_16 = ['summer', 'spring', 'fall', 'winter'] # create a string from this list and separate it with an asterisk

# lower() Converts a string into lower case
day = 'MONDAY'


# partition() Returns a tuple where the string is partitioned into three parts
test_17 = 'I am excited about spring time.'

ex_17 = 'We will be going to the park next week.' # partition this string on the word 'going'

# replace() Returns a string where a specified value is replaced with a specified value
food = 'My favorite food is pizza.'


ex_18 = 'Today is Tuesday. Tuesday we play golf.' # replace instances of Tuesday with Thursday


# split() Splits the string at the specified separator, and returns a list
test_18 = 'I will be broken up on every space'


ex_19 = 'Split*me*up*on*the*asterisk' # split this spring up on every asterisk

# splitlines() Splits the string at line breaks and returns a list
lyrics = "Every time that I look in the mirror\nAll these lines on my face getting clearer\nThe past is gone\nOh, it went by like dusk to dawn\nIsn't that the way?"


# startswith() Returns true if the string starts with the specified value

name = 'giraffe'

ex_20 = 'summer' # Check if this string starts with an 's'

# strip() Returns a trimmed version of the string
username = '   jessica123    '

ex_21 = '  sportsfan876  ' # sanitize this string

'''
Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True
'''

# Get input from user

# Test input

# Provide output



'''
Take a word from the user. Then take a number from the user. Then print whether the word is longer than the number.

Examples:
apple
6
False

python
4
True
'''

# Get user input

# Convert where needed

# Comparison

# Output


'''
Exercise 

Write some code that takes a string from the user, and prints how many vowels are in the string. (Vowels are a, e, i, o, u)
How will you count both uppercase and lowercase vowels?
What string method can you use to count the number of vowels?

Example
User input: Computer
3

'''



'''
You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!

'''


'''
Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
'''

# get input


# get length for top and bottom border

# create output, dont forget to append asterisk to front and back of the string





















