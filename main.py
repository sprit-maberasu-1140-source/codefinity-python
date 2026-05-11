import pandas as pd

def replace_outliers_with_median(df, column, outlier_mask):
    # Your code here
    pass
    median_value = df.loc[~outlier_mask,column].median()

    df.loc[outlier_mask,column] = median_value
# Example usage
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "score": [85, 90, 300, 88, 92]
}
df = pd.DataFrame(data)
outlier_mask = df["score"] > 150

replace_outliers_with_median(df, "score", outlier_mask)
print(df)
