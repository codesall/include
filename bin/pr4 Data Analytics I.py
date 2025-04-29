import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv('bostonhousing.csv')

# Drop missing values
df.dropna(inplace=True)

# Features and Target
X = df.drop('medv', axis=1)
y = df['medv']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction and Evaluation
y_pred = model.predict(X_test)
print(f'Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}')
print(f'R-squared (R²): {r2_score(y_test, y_pred):.2f}')
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)

# Predicting on New Data
new_data = np.array([[0.1, 18, 2.31, 0, 0.4, 6.1, 45, 6.5, 5, 300, 15, 400, 10]])
new_prediction = model.predict(new_data)
print(f'Predicted Home Price for New Data: {new_prediction[0]:.2f}')
