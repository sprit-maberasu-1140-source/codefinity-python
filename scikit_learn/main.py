import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a65bbc96-309e-4df9-a790-a1eb8c815a1c/penguins.csv')
# Missing 値が 2 個以上ある行を除外
df = df[df.isna().sum(axis=1) < 2]

# 1. most_frequent（最頻値）で埋めるインピューターを作成
imputer = SimpleImputer(strategy='most_frequent')
# 2. df[['sex']] の２次元配列に対して補完し、ravel() で一次元にして代入
df['sex'] = imputer.fit_transform(df[['sex']]).ravel()

print(df.head(8))