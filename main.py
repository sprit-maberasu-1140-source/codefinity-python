import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/b22d1166-efda-45e8-979e-6c3ecfc566fc/houses_poly.csv')

# 1. Assign the variables
X = df[['age']]
y = df['price']
n = 2  # Degree

# 2. Preprocess X
X_tilde = PolynomialFeatures(n).fit_transform(X)

# 3. Split
X_tilde_train, X_tilde_test, y_train, y_test = train_test_split(
    X_tilde, y, test_size=0.3, random_state=0
)

# 4. Train model
model = sm.OLS(y_train, X_tilde_train).fit()

# 5. Predictions
y_train_pred = model.predict(X_tilde_train)
y_test_pred = model.predict(X_tilde_test)

# 6. RMSE
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

print("Train RMSE:", train_rmse)
print("Test RMSE:", test_rmse)

# 7. Summary
print(model.summary())