import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
data = sns.load_dataset("titanic")

# 2. Fill missing values
data["age"].fillna(data["age"].mean(), inplace=True)
data["embarked"].fillna(data["embarked"].mode()[0], inplace=True)

# 3. Encode 'sex' and 'embarked' using pd.get_dummies()
data = pd.get_dummies(data, columns=["sex", "embarked"], drop_first=True)

# 4. Scale 'age' and 'fare' using StandardScaler
scaler = StandardScaler()
data[["age_scaled", "fare_scaled"]] = scaler.fit_transform(data[["age", "fare"]])

# 5. Create new column 'family_size'
data["family_size"] = data["sibsp"] + data["parch"] + 1

# Save transformed dataset
transformed_data = data.copy()

print(transformed_data.head())