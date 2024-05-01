import math
# import name_module


# def hello_world():
#     print('Hello World')

# hello_world() # Function call

# Fuction with a print statement
# def greeting(name):
#      print(f'Hello {name}')

# greeting('Sarah') # function call, argument is Sarah

# Function with a return statement
# def greeting(name):
#      return f'Hello {name}'

# print(greeting('Dana')) # to see a returned value, put function call in print statement

# assigning to a variable
# my_name = greeting('Dana')
# print(my_name)

# modify a parameter

# def double_me(value):
#     result = value * 2
#     print(f'{value} doubled is {result}')

# result = double_me(100) # function call assigned to a variable


'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''

# def vowel_or_not(word): # our function, which takes 1 parameter
#     vowel = 'aeiou'
#     for w in word:
#        if w in vowel:
#           print(f'{w} is a vowel')
#        else:
#           print(f'{w} is not a vowel')
       
# tst_string = 'Hollywood' # assign the variable to a string for our function
# vowel_or_not(tst_string) # our function call, passing our variable as an argument


'''
Example

Write a function that returns the surface area of a box (rectangular prism).
Surface Area = width*2 + length*2 + height*2

'''
# def box_surface_area(width, length, height):
#     return 2 *((width*length) + (height * length) + (height * width))

# print(box_surface_area(5, 3, 4))

'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2

'''
# radius = 6.0

# def surface_of_sphere(radius):
#     return 4 * math.pi * radius**2

# print(surface_of_sphere(radius))


''' Lets follow these functions through line by line and analyse the return statements'''

# def print_vowels(word):
#     out = ''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             out += w
    
#     return out

# my_word = 'bananas'

# print_vowels(my_word) # it should return none
# print(get_vowels(my_word)) # this will print the return

# Return is none
def get_vowels(word):
    out = ''
    vowels = 'aeiou'
    for w in word:
        if w in vowels:
            out += w
    
    print(out)

my_word = 'bananas'

# get_vowels(my_word)
# print(get_vowels(my_word)) # Return None



'''
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''

# sample_list = [4,5,3,2,4,3,3,3,3,2,2,1,1,1,1,0,5]
# value = 5

# def val_count(my_list, my_value): # function definition and function name
#     counter = 0
#     while my_value in my_list:
#         my_list.remove(my_value)
#         counter +=1
#         print(my_list)
#         return counter

# result = val_count(sample_list, value) # invoking our function, assigning to a variable
# print(result)


'''
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:
transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}

'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},\
                {'id': 'c', 'amount': 545, 'type': 'deposit'},\
                {'id': 'c', 'amount': 225, 'type': 'withdrawal'},\
                {'id': 'b', 'amount': 45, 'type': 'withdrawal'},\
                {'id': 'e', 'amount': 150, 'type': 'deposit'}]

def transaction_logs(transaction_data):
    output = {}

    for t in transaction_data:
# if ID doesn't yet exist, we will add it to our output dictionary
     if t['id'] not in output.keys():
        if t['type'] == 'deposit': # checking for deposits
           output[t['id']] = t['amount'] # add deposits amount to ID key
     else:
        # Otherwise, it exists, lets check to see if its a withdrawal or deposit
        if t['type'] == 'withdrawal': # checking deposit
           output[t['id']] -= t['amount']
     
print(transaction_logs(transactions)) # our function call, with our list of dictionaries



''' Create a python file called name_module.py. Inside this python file, you will create 3 functions. One called full_name, another called reverse_name, and a third called get_initials. Each function will take 2 strings. One string will be the first name, the second string will be the last name. full_name will concatenate and return the full name. For example if the first string is "Joseph" and the second string is "Simpson" This function will return the string, "Joseph Simpson". Reverse name will flip the name around. The name Diana Prince, would come back as Prince Diana. The third function will take the first and last name and return the initials. The name Tony Stark will return T.S. Now create a second python file, called name.py. Import the module you just created and call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal'''

