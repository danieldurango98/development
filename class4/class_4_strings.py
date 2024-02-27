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
# greeting = 'hip hip hooray ' * 3
# print(greeting)

''' Using multiplication, create a new string that multiplies your favorite color 5 times'''

# color = 'blue ' * 5
# print(color)

# Reference vs Value equality  == vs is
x = 'hello'
str2 = 'HELLO'.lower()
# print(x)
# print(str2)
# print(x == str2)
# print(x is str2)
# print(id(x))
# print(id(str2))

''' in - Returns True if a string appears inside another string (as a substring), and False otherwise.'''
# test_character = 'b'
# test_string = 'bananas'
# print(test_character in test_string) #?

''' create a quick test to see if the sub string 'spreh' can be found in the string 'Incomprehensibilities' '''
test_chars = 'spreh'
test_word = 'Incomprehensibilities'

# print(test_chars in test_word)



''' len() - Returns the length of a string, aka the number of characters in a string.'''
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# length_of_alphabet = len(alphabet)
# print(length_of_alphabet)


''' create a variable that holds a string of your favorite animal, create a variable to capture the length of that animal's string value'''
# animal = 'zebra'
# length_of_animal = len(animal)
# print(length_of_animal)

# String methods

word_1 = 'happy' # capitalize me!
# print(word_1.capitalize())
# print('happy'.capitalize())

ex_1 = 'cereal' # capitalize me!
# print(ex_1.capitalize())

word_2 = 'SuPrISe' # make me lower case!
# print(word_2.casefold())

ex_2 = 'RuMMaGe' # make me lower case!
# print(ex_2.lower())
# print('RuMMaGe'.lower())

word_3 = 'ZOO' # make me lower case!
# print(word_3.lower())

ex_3 = 'PLANET' # make me lower case!
# print(ex_3.casefold())
# print('PLANET'.casefold())

'''FUN FACT: Whereas casefold() method is an advanced version of lower() method, it converts the uppercase letter to lowercase including some special characters which are not specified in the ASCII table for example ‘ß’ which is a German letter and its lowercase letter is 'ss'.
'''

word_4 = 'Good Evening'
# print(word_4)
# print(word_4.center(100)) # Takes up 100 characters and centers the string
# print(word_4.center(50))

ex_4 = 'Hello World!' # center me within a space of 65 characters
# print(ex_4.center(65))

word_5 = 'Pseudopseudohypoparathyroidism' # How many p's? # count is case sensitive
# print(word_5.count('p'))

ex_5 = 'Antidisestablishmentarianism' # how many times does the letter 'e' occur?
# print(ex_5.count('e'))

word_6 ='I\tam\ta\ttab' # extendtabs
# print(word_6)
# print(word_6.expandtabs(10))

# create_new_line = 'I\n am\n a\ newline'
# print(create_new_line)

ex_6 = "Let's\t do\t some\t coding!" # lets try to increase the tabs to 10 whitespaces
# print(ex_6.expandtabs(15))

# Find the position of the letter k
word_7 = 'Omphaloskepsis'
# print(word_7.find('k'))


ex_7 = 'Dichlorodifluoromethane' # find the position of the letter f
# print(ex_7.index('f'))

word_8 = 'Supercalifragilisticexpialidocious'
# print(word_8.find('g'))

'''Fun Fact - Both index() and find() are identical in that they return the index position of the first occurrence of the substring from the main string. The main difference is that Python find() produces -1 as output if it is unable to find the substring, whereas index() throws a ValueError exception.'''


# isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z and 0-9

test_1 = 'abcdef'
test_2 = '%$123'

# print(test_1.isalnum())
# print(test_2.isalnum())

ex_8 = '123*' # Am I alphanumeric?
# print(ex_8.isalnum())

# isalpha() Are all characters in the string in the alphabet?

test_3 = 'abcde'
test_4 = '012345'

# print(test_3.isalpha())
# print(test_4.isalpha())

ex_9 = 'LMN0P' # Are we all in the alphabet
# print(ex_9.isalpha())

# isdecimal() Are all characters decimals?

test_5 = '1234P'
test_6 = '234567'

# print(test_5.isdecimal())
# print(test_6.isdecimal())

ex_11 = '123456' # Check for decimals?
# print(ex_11.isdecimal())

# isdigit() Are all characters digits?

test_7 = 'H1234'
test_8 = '9876'

# print(test_7.isdigit())
# print(test_8.isdigit())

ex_10 = '123Hello' # Check for digits!
# print(ex_10.isdigit())

''' Fun fact isdecimal() method supports only Decimal Numbers. isdigit() method supports Decimals, Subscripts, Superscripts. 
isnumeric will check for unicode characters
'''


# islower() Lets check for lowercase

test_9 = 'Zebra'
test_10 = 'affordable'
# print(test_9.islower())
# print(test_10.islower())


ex_12 = 'Username' # check if all lowercase

# isupper() lets check for ALL uppercase

test_11 = 'Marshall'
test_12 = 'HALLOWEEN'
# print(test_11.isupper())
# print(test_12.isupper())

ex_13 = 'TEMPLE' # check if uppercase

# isspace() Lets check for whitespace (someone enters nothing for an input)

test_13 = '    '
test_14 = 'j      b    c'
# print(test_13.isspace())
# print(test_14.isspace())

ex_14 = '   ' # check if whitespace


# istitle() Let's check for title case

test_15 = 'Eye of the tiger'
test_16 = 'Eye Of The Tiger'

# print(test_15.istitle())
# print(test_16.istitle())

ex_15 = 'Tempus Fugit' # check for title casing

# join() Joins the elements of an iterable to the end of the string

my_colors = ['blue', 'green', 'red', 'orange', 'blue'] # list datatype
new_string = '-'.join(my_colors)
# print(new_string)

ex_16 = ['summer', 'spring', 'fall', 'winter'] # create a string from this list and separate it with an asterisk

# lower() Converts a string into lower case
day = 'MONDAY'
new_day = day.lower()
# print(new_day)

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

# strip() Returns a trimmed version of the string  cleans data
username = '   jessica123    '
username_cleaned = username.strip()
# print(len(username))
# print(len(username_cleaned))

ex_21 = '  sportsfan876  ' # sanitize this string

#user_input = int(input('What is your favorite number? ')) 

# print(int(user_input)) # casting the string to an integer
# print(type(user_input))

'''
Write some code that will take a string from the user and print if it is a number or not.

Examples:   #ex_10 = '123Hello' # Check for digits!
print(ex_10.isdigit())
apple
False

4
True
'''

# Get input from user # input statement

user_input = input('Good afternoon, please enter your input: ')

# Test input 
result = user_input.isdigit()
print(result)

# Provide output
print('Is your input a number or not?', result)


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





















