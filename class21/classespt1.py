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


# creating the object of the Point2D Class
point1 = Point2d(4,10)
point2 = Point2d(8,15)

# Return a string representation of this object
# print(point1)
# print(point2)   
    
# Adds this object to another object from the same class, return a new object.
# print(point1 + point2)    
    
# Subtracts another object from this object, return a new object.
print(point1 - point2)    

# Test equality between this object and another, return a boolean.
   
     
    
# Mutator method
  

# Accessor method
   

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





''' Exercise - Date Class '''




 




'''
Exercise - Dog Class
'''






