import pandas as pd

def standardize_column_case(df, column_name):
    # 1. 元の表をそのまま残すためにコピーを作ります
    df = df.copy()
    # 2. 指定された列(column_name)の文字をぜんぶ小文字にします
    df[column_name] = df[column_name].str.lower()
    # 3. 小文字に直した表を返します
    return df

data = {
    "Response": ["Yes", "no", "YES", "No", "yes", "NO", "nO", "YeS"]
}
df = pd.DataFrame(data)
result = standardize_column_case(df, "Response")
print(result)