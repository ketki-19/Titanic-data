import pandas as pd

# Load data
df = pd.read_csv("train.csv")

#first 5 rows
print("\nFirst 5 rows")
print(df.head())

#last 5 rows
print("\nLast 5 rows")
print(df.tail())

#Data frame info
print("\n Dataframe INFO:\n")
df.info()

#Statistical Summary
print("\n Statistical Summary \n")
print(df.describe())

categorical_cols = ["Sex", "Embarked", "Pclass", "Cabin", "Ticket"]

for col in categorical_cols:
    print(f"\n Unique values in {col}: ")
    print(df[col].value_counts())