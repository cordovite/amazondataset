import pandas as pd

# Load the dataset (make sure the file name matches exactly)
df = pd.read_csv("Amazon_Unlocked_Mobile_Sample.csv")

# print(df.head())

# print(df.info())

# top_rated = df.groupby('Product Name').agg({
#     'Rating': 'mean',
#     'Reviews': 'count'
# }).query('Reviews >= 10').sort_values(by='Rating', ascending=False)

# print("\nTop 5 highest-rated phones (with 10+ reviews):")
# print(top_rated.head(5))

print(df['Rating'].value_counts())

