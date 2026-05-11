import pandas as pd
import numpy as np

def detect_missing(dataframe):
    # dataframe の中で「欠けている値（NaN）」を探して
    # 同じ形の True/False の表を返す
    return dataframe.isna()

# 動作確認用のサンプルデータ
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, np.nan, 30, 22],
    "City": ["New York", "Los Angeles", np.nan, "Chicago"],
    "Score": [85, 90, np.nan, 88]
}
df = pd.DataFrame(data)

result = detect_missing(df)
print(result)