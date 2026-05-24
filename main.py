import pandas as pd

def oversample_minority(df, target_column):
    class_counts = df[target_column].value_counts()
    max_count = class_counts.max()
    classes = class_counts.index.tolist()
    balanced_df_list = []
    for cls in classes:
        class_subset = df[df[target_column] == cls]
        if len(class_subset) < max_count:
            oversampled_subset = class_subset.sample(max_count, replace=True, random_state=42)
        else:
            oversampled_subset = class_subset
        balanced_df_list.append(oversampled_subset)
    balanced_df = pd.concat(balanced_df_list).reset_index(drop=True)
    return balanced_df

# Example usage
data = {
    "feature1": [1, 2, 3, 4, 5, 6],
    "target": ["A", "A", "A", "B", "B", "B"]
}
df = pd.DataFrame(data)
# Remove one "B" to create imbalance
df = df.iloc[:-1]

balanced_df = oversample_minority(df, "target")
result_shape = balanced_df.shape
result_counts = balanced_df["target"].value_counts()
print(result_shape)
print(result_counts)