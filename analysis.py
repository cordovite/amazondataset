import pandas as pd

# Load the dataset (make sure the file name matches exactly)
df = pd.read_csv("Amazon_Unlocked_Mobile_Sample.csv")

# Show the first 5 rows
print(df.head())

# Check the columns and data types
print(df.info())
