import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load data
df = pd.read_csv('Social_Network_Ads.csv')
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# Scaling and splitting
X_train, X_test, y_train, y_test = train_test_split(StandardScaler().fit_transform(X), y, test_size=0.25, random_state=0)

# Model
model = LogisticRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

# Metrics
cm = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = cm.ravel()
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Results
print(f"Confusion Matrix:\n{cm}")
print(f"TP:{TP} FP:{FP} TN:{TN} FN:{FN}")
print(f"Accuracy:{accuracy:.2f} Error Rate:{error_rate:.2f} Precision:{precision:.2f} Recall:{recall:.2f}")
