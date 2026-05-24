import pandas as pd

def undersample_majority_class(df, target_col):
    # 各クラスのサンプル数を取得
    class_counts = df[target_col].value_counts()
    
    # クラスが2つでない場合はそのまま返す
    if len(class_counts) != 2:
        return df.copy().reset_index(drop=True)
    
    # 少数派・多数派クラスを判定
    minority_class = class_counts.idxmin()
    majority_class = class_counts.idxmax()
    n_minority = class_counts.min()
    
    # すでにバランス済みならシャッフルして返却
    if class_counts.min() == class_counts.max():
        return df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # 少数派・多数派を分割
    df_minority = df[df[target_col] == minority_class]
    df_majority = df[df[target_col] == majority_class]
    
    # 多数派をランダムにアンダーサンプリング
    df_majority_undersampled = df_majority.sample(n=n_minority, random_state=42)
    
    # 結合→シャッフル→インデックスリセット
    df_balanced = pd.concat([df_minority, df_majority_undersampled])
    return df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

data = {
    "feature": [1, 2, 3, 4, 5, 6, 7, 8],
    "target":  ["A", "A", "A", "A", "B", "B", "B", "B"]
}
df = pd.DataFrame(data)

df_imbalanced = pd.concat(
    [df, pd.DataFrame({"feature": [9, 10], "target": ["A", "A"]})],
    ignore_index=True
)
balanced_df = undersample_majority_class(df_imbalanced, "target")
print(balanced_df)