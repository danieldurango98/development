''' Lists '''


# Indexing
# planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter']
# first_planet = planets[0] # bracket notation can be assigned to a variable
# print(first_planet)
# print(planets[0])
# print(planets[1])
# print(planets[2])
# print(planets[3])
# print(planets[4])
# print(planets[5])
# print(planets[6]) # Lets take a note of the error message

# Update with indexing
# colors = ['red', 'green', 'yellow', 'blue', 'orange']
# print('first list',colors)
# colors[0] = 'black'
# colors[1] = 'orange'
# print('after update',colors)

# my_color = colors.index('blue') # this will deliver a value of 3
# print(my_color)


# Iterate with for loop
# animals = ['dog', 'cat', 'lion', 'tiger', 'eagle']

# for a in animals:
#     print(a)


# Len function gives us the amount of items in a list
# modes_of_travel = ['car', 'plane', 'truck', 'train', 'boat']
# how_many_vehicles = len(modes_of_travel)
# print(how_many_vehicles)
# print(len(modes_of_travel))

'''
Exercise

Create a for loop that goes through a list and prints each item in the list, along with its index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars

'''
# planets = ["mercury", "venus", "earth", "mars"]

# how_many_planets = len(planets)
# print(how_many_planets)

# counter = 0

# for a in planets:
#     print(f'{counter}: {a}',end=' ')
#     counter += 1


''' Exercise
Write some code that takes one list and creates a second list that has the type for each entry in the list. Hint: Use the type() function and a for loop

Optional:
Make sure you filter out any repeats.

data = ['car', 3, True, False, 4.09, 'Tuesday']

'''

# fname = 'Annie'
# is_warm_out = True
# temp = 98

# print(type(fname))
# print(type(is_warm_out))
# print(type(temp))

# Our collections

''' The Append Method will allow you to add values to a list'''

# data = ['car', 3, True, False, 4.09, 'Tuesday']
# types_list = [] # This list will hold our types

# Looping through for types

# for d in data:
#     types_list.append(type(d)) # grabbing the types from data, appending to empty list
# print('Our Types List which contains duplicates', types_list)

# Optional, remove repeats using sets
# types_list = list(set(types_list))
# print('Duplicates removed with sets', types_list)

''' List Methods '''

'''
append() Adds an element at the end of the list
clear() Removes all the elements from the list
copy() Returns a copy of the list
count() Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list

'''

food = ['ice cream', 'pizza', 'apple', 'burger', 'cookies']

# lets add salad with append
# food.append('salad')
# print(food)

# lets remove all items with clear
# food.clear()
# print(food)


# let create a copy
# new_food_list = food.copy()
# food.append('asparagus')
# print('This is our copy', new_food_list)
# print('This is our oringal list', food)

# How many times does pizza appear? count method
# pizza_count = food.count('pizza')
# print(pizza_count)

# Lets add items of a list to our food list, extend
# vegetables = ['carrots', 'asparagus', 'broccoli']
# food.extend(vegetables)
# print(food)

# lets find the index value for apple
# print('This index of the apple is', food. index('apple'))

# Lets add cereal to the 3rd spot in our list insert method
# food.insert(3, 'cereal')
# print(food)

# Lets remove a food by index position pop method
# food.pop(1)
# print(food)

# Lets remove an item with a specified value 
# food.remove('burger')
# print(food) # it will only remove the first instance

# food.remove('ice cream')
# print(food)

# Lets reverse our list
# food.reverse()
# print(food)

# Lets sort our list
# food.sort()
# print(food)

# Sort versus sorted()

# Sorted returns a newer sorted list
# new_sorted_list = sorted(food)
# print(new_sorted_list)



'''
Exercise: List of Pets

You want to make a list containing the types of pets that the user has. Keep prompting the user for a pet until they enter "stop". If it's a new pet, add it to the list. If the list already has that pet, don't add it.

'''

# user_input = '' # initialization
# pet_name = [] # this will capture animal names

# while user_input != 'stop':
#     user_input = input('Please enter your pets name: ')
#     if user_input == 'stop': # this is to not add stop to the list
#         break
#     elif user_input not in pet_name:
#         pet_name.append(user_input)
#     else:
#         print(f'{user_input} is already in the list')

# print(pet_name)

''' Removing duplicates from a list, but leaving 1'''

colors = ['blue', 'blue', 'blue', 'green', 'red', 'blue', 'blue']

# Option 1 
# new_colors = [] # this will capture unique colors
# for c in colors: # this is looping through original list
#     if c not in new_colors:
#         new_colors.append(c)
# print(new_colors)

# Option 2 - Using Sets
# colors = list(set(colors))
# print(colors)



'''
Example: Removing Values
You have a list of numbers, but it contains multiple of the number 2. Remove the number 2 until it only appears in the list once.

num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5]
'''
num_values = [2, 3, 4, 3, 2, 2, 2, 4, 1, 3, 4, 5, 2, 2, 2, 2] # removes an item based on its value. If there are multiple, it removes the first item with that value.


# Option 1


# Option 2





'''
You have a list storing important data for your company, but it contains some duplicate entries. Go through your list and remove all the duplicates. When you're done, each item should appear in the list exactly once.
Hint: How would you expand our previous example, which removed duplicates of one value, to remove duplicates of all values?
Hint 2: You might want to make a copy of the original list to use as reference. You may want to use more than one loop.

transaction_dates = []
'''

transaction_dates = ['3/5/2024', '3/5/2024', '5/4/2019', '2/23/2023', '5/4/2019','5/2/2023', '2/23/2023', '2/23/2024', '8/6/2019', '5/4/2019','3/5/2024','5/2/2023']




# Using sets

