import pandas as pd

def impute_with_mean(df, column):
    # Your code here
    mean_value = df[column].mean()
    df[column] = df[column].fillna(mean_value)
    return df
# Example usage:
data = {
    "id": [1, 2, 3, 4, 5],
    "score": [85, None, 78, None, 92]
}
df = pd.DataFrame(data)
df_imputed = impute_with_mean(df, "score")
print(df_imputed)
