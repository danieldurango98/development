''' Loops '''

''' While Loops '''

''' While my start value is less than my end value, we will increment by 1'''



''' While my start value is less than my end value, we will decrement by one - You can stop the infinite loop by hitting ctrl + c'''



''' Example Create a while loop that prints every integer from 1 to 10.'''



'''
While Loops and User Input

While loops are often paired with user input. The condition for the loop might be what the user needs to enter to stop the loop. The user is prompted for input each time it loops, and something happens based on that input.
This allows you to take user input multiple times without writing multiple lines of input(). It also allows the user to control how much input they give.

Lets look at code that will run infinitely until the user tells it to "stop"
'''


'''
Exercise

Improve the login system we wrote last class to allow multiple attempts. You're developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.


'''

# Set sys id and pass


# Prompt User


# Our initial check, while not equal we will enter loop



''' For Loops '''

# STRING
my_string = 'Supercalifragilisticexpialidocious'


# LIST
my_list = ['dog', 'cat', 'bird', 'giraffe', 'fox', 'elephant', 'mouse', 'zebra']


# TUPLE
my_tuple = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')



# DICTIONARY
my_dictionary = {"First name": "Jill",
                 "Last name": "Simmons",
                 "Age": 34,
                 "Address":"1515 Mockingbird Lane"}




# SET
my_set = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}



# RANGE



'''
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.
'''



''' Exercise

Take a string from the user. Verify that it's a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop
'''




''' Exercise 
Write some code that will loop through a string and print whether each letter is a vowel or consonant.

Example:
'hello'
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel


'''




''' Exercise 
You're working on a data analysis project for a company that looks at written text. You're only interested in letters from A-Z because you're analyzing language. However, the data you're given has some values that shouldn't be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn't a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''










