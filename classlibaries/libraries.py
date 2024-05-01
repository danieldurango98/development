import math
import statistics as st
import pandas as pd

from datetime import date
import datetime as dt
import requests

'''
Example
Import the math library.
Take the radius of a circle as user input.
Then, compute the area of the circle using the math library.
'''

# raduis = int(input("What is the raduis? "))
# area = math.pi * raduis**2
# print(area)


# BONUS

# lets do a try except just in case the user enters letters
# try:
#   raduis = int(input("What is the raduis? "))
#   area = math.pi * raduis**2
#   print(area)
# except ValueError:
#   print('Invalid input, numbers only')


'''
Exercise
Lets make some magic happen with the statistics library.
'''


# With Statistics Library

''' Nice little mean calculator to help with our testing

https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php
'''

# middle value in odd numbered list
# odd_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
# median_of_an_odd_list = st.median(odd_list)
# print(median_of_an_odd_list)

# # # average of two middle values
# even_list = [1, 2, 3, 4, 5, 2, 9, 1, 3, 4, 6, 7]
# median_of_an_even_list = st.median(even_list)
# print(median_of_an_even_list)


'''
Exercise
Lets make some magic happen with the pandas library.
'''
# # dictionary with my users our favorite dog
canines = {
  "dog_name": ['saige', 'benji', 'stella', 'zuzu'],
  "dog_breed": ['dachsund', 'mastiff', 'golden retriever', 'hound'],
}


# load into a dataframe
df = pd.DataFrame(canines)
# print(df)

# I can even loop through it!
# for index, row in df.iterrows():
#     print(f'{row['dog_name']} is {row['dog_breed']}')

# Or assign a variable to a column and loop through that
# dog_name = df['dog_name']
# for d in dog_name:
#     print(d)

# generate a csv # also known as a flat file

# df.to_csv('output.csv', index=False)


'''
Exercise
Lets make some magic happen with the date time library.
'''
today = date.today()
print(today)
print(f'Today is {today}')
print(f'The day is {today.day}')
print(f'The month is {today.month}')
print(f'The year is {today.year}')
last_week = today + dt.timedelta(days=-7)
print(last_week)

'''
https://jsonplaceholder.typicode.com

This website provides free api testing. Lets leverage python's request module to see if we can do a get request against this data
'''
my_response = requests.get('https://jsonplaceholder.typicode.com/todos')

print(my_response.text)

