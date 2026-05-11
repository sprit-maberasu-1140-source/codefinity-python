import pandas as pd

def drop_missing_rows(df):
    # ここで欠けているデータを含む行を取り除きます
    return df.dropna()

# 動作確認用のサンプルデータ
import numpy as np
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, np.nan, 30, 22],
    "city": ["New York", "Los Angeles", np.nan, "Chicago"]
}
df = pd.DataFrame(data)

# 関数を呼び出して結果を表示
result = drop_missing_rows(df)
print(result)