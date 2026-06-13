import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/b22d1166-efda-45e8-979e-6c3ecfc566fc/houseprices.csv')
# Assign the variables
X = df[['age', 'square_feet']]
y = df['price']
# Preprocess X
X_tilde = sm.add_constant(X)
# Build and train the model
model = sm.OLS(y, X_tilde).fit()
# Create and preprocess X_new
X_new = np.array([[4, 10000], [30, 14000], [70, 16000]])
X_new_tilde = sm.add_constant(X_new)
# Predict instances from X_new and print them
y_pred = model.predict(X_new_tilde)
print('Prediction:', np.floor(y_pred)) # np.floor() keeps only the whole part of the numbers
# Print the summary table
print(model.summary())