import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier

# データ読み込み＆前処理
df = pd.read_csv(
    'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/'
    'a65bbc96-309e-4df9-a790-a1eb8c815a1c/penguins.csv'
)
df = df[df.isna().sum(axis=1) < 2]
X = df.drop('species', axis=1)
y = df['species']

# 目的変数のエンコード
label_enc = LabelEncoder()
y = label_enc.fit_transform(y)

# 特徴量の前処理パイプライン
ct = make_column_transformer(
    (OneHotEncoder(), ['island', 'sex']),
    remainder='passthrough'
)
pipe = make_pipeline(
    ct,
    SimpleImputer(strategy='most_frequent'),
    StandardScaler(),
    KNeighborsClassifier()
)

# 学習・予測・出力
pipe.fit(X, y)
y_pred = pipe.predict(X)
print(label_enc.inverse_transform(y_pred))