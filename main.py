import pandas as pd

def remove_duplicates(df):
    # Your code here
    return df.drop_duplicates()

# Sample DataFrame for testing
data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "Age": [25, 30, 25, 35, 30],
    "City": ["New York", "Paris", "New York", "London", "Paris"]
}
df = pd.DataFrame(data)

result = remove_duplicates(df)
print(result)
