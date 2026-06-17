import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# データ読み込み・前処理
df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a65bbc96-309e-4df9-a790-a1eb8c815a1c/penguins.csv')
df = df[df.isna().sum(axis=1) < 2]  # 欠損値が2つ以上の行を削除
X, y = df.drop('species', axis=1), df['species']

# 1. ターゲットをエンコード
label_enc = LabelEncoder()
y = label_enc.fit_transform(y)

# 2. 訓練／テスト分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 3. カラム変換器の作成
ct = make_column_transformer(
    (OneHotEncoder(), ['island', 'sex']),
    remainder='passthrough'
)

# 4. パラメータグリッドの定義
param_grid = {
    'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15],
    'weights': ['uniform', 'distance'],
    'p': [1, 2]
}

# 5. グリッドサーチのセットアップ
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid)

# 6. パイプラインの構築
pipe = make_pipeline(
    ct,
    SimpleImputer(strategy='most_frequent'),
    StandardScaler(),
    grid_search
)

# 7. モデル学習
pipe.fit(X_train, y_train)

# 8. テスト精度の表示
print("Test score:", pipe.score(X_test, y_test))

# 9. 予測と逆エンコード
y_pred = pipe.predict(X_test)
print("Predictions (first 5):", label_enc.inverse_transform(y_pred[:5]))

# 10. 最適推定器の表示
print("Best estimator:", grid_search.best_estimator_)