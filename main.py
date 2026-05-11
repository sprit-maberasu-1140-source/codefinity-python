import pandas as pd

def count_duplicates(df):
    # Your code here
    pass

    return df.duplicated().sum()

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"],
    "Age": [25, 30, 25, 35, 30, 25],
    "City": ["NY", "LA", "NY", "SF", "LA", "NY"]
}
df = pd.DataFrame(data)

result = count_duplicates(df)
print(result)
