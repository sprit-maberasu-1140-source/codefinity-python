import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

# データの読み込み
df = pd.read_csv(
    'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a65bbc96-309e-4df9-a790-a1eb8c815a1c/penguins.csv'
)

# 欠損値が2つ以上ある行を削除
df = df[df.isna().sum(axis=1) < 2]

# 説明変数Xと目的変数yに分割
X, y = df.drop('species', axis=1), df['species']

# sex, islandのみOneHotでエンコードし、他の列はそのまま残すColumnTransformerを作成
ct = make_column_transformer(
    (OneHotEncoder(), ['sex', 'island']),
    remainder='passthrough'
)

# ColumnTransformer → 欠損値補完 → 標準化 の順で実行するパイプラインを構築
pipe = make_pipeline(
    ct,
    SimpleImputer(strategy='most_frequent'),
    StandardScaler()
)

# Xを変換してX_transformedに保存
X_transformed = pipe.fit_transform(X)
print(X_transformed)