import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/b22d1166-efda-45e8-979e-6c3ecfc566fc/houses_simple.csv')
# Assign the variables
X = df['square_feet']
y = df['price']
# Preprocess X
X_tilde = sm.add_constant(X)
# Build and train a model
regression_model = sm.OLS(y, X_tilde).fit()
# Create and preprocess X_new
X_new = np.array([1300, 10000, 25000])
X_new_tilde = sm.add_constant(X_new)
# Predict the target for X_new
y_pred = regression_model.predict(X_new_tilde)
# Plot the data points and prediction line
plt.scatter(X, y, alpha=0.5)
plt.plot(X_new, y_pred, color='red')
plt.show()
print(y_pred)