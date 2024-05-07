from datetime import datetime
import datetime

'''
Classes
'''
# Class Definition and Initializer
class Point2d:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    '''String Representation'''
    def __str__(self):
        return f'({self.x},{self.y})'  
      
# Add your object to another object of your class
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)    
    
# Subtract my object from another object
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    
# Test equality between this object and another
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
# Less than function
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
# Mutator Method - Setter

    def set_x(self, new_x):
        self.x = new_x

# Mutator Method for y

    def set_y(self, new_y):
        self.y = new_y

# Accessor Method for x
    def get_x(self):
        return self.x
    
# Accessor Method for y   
    def get_y(self):
        return self.y


# creating the object of the Point2D Class
point1 = Point2d(4,10)
point2 = Point2d(8,15)

# Return a string representation of this object
# print(point1)
# print(point2)   
    
# Adds this object to another object from the same class, return a new object.
# print(point1 + point2)    
    
# Subtracts another object from this object, return a new object.
# print(point1 - point2)    

# Test equality between this object and another, return a boolean.
point3 = Point2d(3,4)
point4 = Point2d(3,4)
# print(point3 == point4)   


# Less than function
point5 = Point2d(10, 12)
point6 = Point2d(13, 15)
# print(point5 < point6)
     
    
# Mutator method
point7 = Point2d(5,11)
point7.set_x(10) # our method will change the value of x
# print(point7)

point7.set_y(25)
# print(point7)

# Accessor Method for x
# print(point7.get_x())

# Accessor Method for y
# print(point7.get_y())


''' Excercise - Dog Class
This class will take 3 parameters, dog name, dog breed, and age (human years)
'''

class Dog:
    
    def __init__(self, name, birth_year, breed):
        self.name = name
        self.birth_year = birth_year
        self.breed = breed

    def __str__(self):
        return f'{self.name} is a {self.breed} and was born in {self.birth_year}'
    
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        return f'{self.name} is {year - self.birth_year} years old in human years.'
    
    
# Write a method that will calculate dog years    
    def dog_years(self):
        today = datetime.datetime.now()
        year = today.year
        return f'{self.name} is {(year - self.birth_year) * 7} years old in dog years'
    
    
    def human_age(self):
        today = datetime.datetime.now()
        year = today.year
        return year - self.birth_year

    def dog_years(self):
        dog_years = 7 * self.human_age()
        return f'{self.name} is {dog_years} in dog years'

    

dog1 = Dog('Fido', 2020, 'Golden Retriver') # Created our first object of the dog class
dog2 = Dog('Zuzu', 2021, 'Dachsund' )
dog3 = Dog('Stella', 2016, 'Japanese Chin')

# String representation
# print(dog1)
# print(dog2)
# print(dog3)

# Human Age Method
# print(dog1.human_age())
# print(dog2.human_age())
# print(dog3.human_age())

# Dog Age Method
# print(dog1.dog_years())
# print(dog2.dog_years())
# print(dog3.dog_years())




# today = datetime.datetime.now()
# year = today.year
# print(year)


# Create a point object with attributes x=2, y=3

# Let’s add a __str__ method to our Point2D class so we can print Point2D objects.


# Lets add __add__ to add objects of the same class together


# Lets try __sub__ to add objects of the same class together

# Let's try __eq__ method to test equality
'''What is the output of this code if we don't override ==?
What is the output if we override == to use value equality?
Is it the same or different? Why?

Without the __eq__ method, we will only be able to test if it is the same object
'''



# Let's try __lt__ method to test less than


# Setting with mutator methods



# Getting with accessor methods





''' Exercise - Date Class 

1. Display the date in a format of mm/dd/yyyy
2. Compare 2 different dates, if they are equal
3. Compare which date came first
4. Determine if a date is a leap year

'''

class Date:
    
    def __init__(self, year=1970, month=1, day=1):
        ''' These are our parameters '''
        self.year = year
        self.month = month
        self.day = day
    # this will control what the print built in function displays
    def __str__(self):
        return f'Month: {self.month:02d}\nDay: {self.day:02d}\nYear: {self.year}'
    # this will control what == does in your class
    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False


my_date_info = Date(2004, 10, 4) # created the object
second_date = Date(2004, 10, 4)

# String representation
# print(my_date_info)

# equality
print(my_date_info == second_date)

 




'''
Exercise - Dog Class
'''






