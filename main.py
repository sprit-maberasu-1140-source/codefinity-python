import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1. Define preprocessing function
def preprocess_titanic(data):
    # 2. Fill missing values
    for col in data.columns:
        if data[col].dtype in ["float64", "int64"]:
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)

    # 3. Encode categorical columns
    data = pd.get_dummies(data, columns=["sex", "embarked"], drop_first=True)

    # 4. Scale 'age' and 'fare'
    scaler = StandardScaler()
    data[["age_scaled", "fare_scaled"]] = scaler.fit_transform(data[["age", "fare"]])

    # 5. Create new feature
    data["family_size"] = data["sibsp"] + data["parch"] + 1

    return data

# 6. Load dataset and apply pipeline
titanic = sns.load_dataset("titanic")
processed_data = preprocess_titanic(titanic)

print(processed_data.head())