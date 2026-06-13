import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv(
    'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/'
    'b22d1166-efda-45e8-979e-6c3ecfc566fc/houses_poly.csv'
)

# 1. 説明変数 X に 'age' 列を DataFrame 形式で代入
X = df[['age']]
y = df['price']
n = 2  # 多項式の次数

# 2. PolynomialFeatures で 1, x, x^2 の特徴量に変換
X_tilde = PolynomialFeatures(n).fit_transform(X)

# 3. OLS モデルを構築して学習
model = sm.OLS(y, X_tilde).fit()

# 4. 予測用データを生成し、2 次元配列に変形
X_new = np.linspace(0, 125, 200).reshape(-1, 1)

# 5. X_new を同様に多項式変換
X_new_tilde = PolynomialFeatures(n).fit_transform(X_new)

# 6. 予測と可視化
y_pred = model.predict(X_new_tilde)
plt.scatter(X, y, alpha=0.4)
plt.plot(X_new, y_pred, color='orange')
plt.show()

# 7. モデルの係数を出力
print(model.params)