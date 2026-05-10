import seaborn as sns
import pandas as pd

# 1. 船のデータを読み込む
data = sns.load_dataset("titanic")

# 2. age（年齢）の空欄を年齢の平均で埋める
mean_age = data["age"].mean()
data["age"].fillna(mean_age, inplace=True)

# 3. embarked（乗船した港）の空欄をいちばん多い値（モード）で埋める
mode_port = data["embarked"].mode()[0]
data["embarked"].fillna(mode_port, inplace=True)

# 4. 全く同じデータが重複していたら削除する
data.drop_duplicates(inplace=True)

# 5. fare（料金）のとびぬけた値（外れ値）をIQR法で取り除く
Q1 = data["fare"].quantile(0.25)
Q3 = data["fare"].quantile(0.75)
IQR = Q3 - Q1
cleaned_data = data[
    (data["fare"] >= Q1 - 1.5 * IQR) &
    (data["fare"] <= Q3 + 1.5 * IQR)
]

# 結果を表示
print(cleaned_data.info())