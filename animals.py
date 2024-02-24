import pandas as pd # Import for pandas library

animals = ['Lions', 'Tigers', 'Bears', 'Dogs', 'Cats'] # List Collection

df = pd.DataFrame(animals) # Convert our list to a format to which Pandas can use

print(df)