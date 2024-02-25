''' This program calculates the perimeter of a triangle

Requirements
    - Comment your code 
        +5
    - Assign meaningful variable names 
        +5
    - Output a print statement, "The perimeter of your triangle is..." 
        +5
    - The test case for your program is side # 1 is 5, the base is 6, side # 2 is 10 
        +5
    - Output a print statement, "Is side 1 greater than side 2?" 
        +5
    - Output a print statement, "Is the base equal to side 1?"
        +5
'''
side_one = 5
side_two = 10 # assigning variable names to the triangle's sides
base = 6

perimeter = side_one + side_two + base  # formula to calulate the perimeter of the triangle
print(perimeter)
print(type(perimeter)) # finding the class type

print('The perimeter of your triangle is',perimeter)  # Output statement

print(side_one > side_two)  # figuring out if side 1 is greater than side 2
print(base == side_one) # figuring out if the base is equal to side 1

