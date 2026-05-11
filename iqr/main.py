import pandas as pd

def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    # ステップ1: データを小さい順に並べて、下から25％のところ（Q1）と上から25％のところ（Q3）を見つける
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    # ステップ2: Q3 − Q1 を計算して IQR（データの真ん中50％の広がり）を求める
    iqr = q3 - q1
    # ステップ3: 下限と上限を決める
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    # ステップ4: 元の値が下限より小さいか、上限より大きいかを調べて True/False を返す
    return (series < lower_bound) | (series > upper_bound)

# 使い方の例
data = {"score": [10, 12, 13, 14, 15, 16, 17, 18, 100, 110]}
df = pd.DataFrame(data)
outliers = detect_outliers_iqr(df["score"])
print(outliers)