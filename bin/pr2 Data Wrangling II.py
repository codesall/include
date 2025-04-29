import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler

data = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math_Score': [88, 92, 95, 100, 67, 73, np.nan, 85, 110, 89],
    'Science_Score': [78, 85, 90, 75, 70, 80, 82, 95, 120, np.nan],
    'English_Score': [80, 79, 85, 83, 77, 75, 70, 88, 60, 90],
    'Attendance_Percent': [95, 98, 100, 60, 88, 85, 90, 92, 105, 75]
}

df = pd.DataFrame(data)

print("Missing Values:")
print(df.isnull().sum())

df['Math_Score'].fillna(df['Math_Score'].mean(), inplace=True)
df['Science_Score'].fillna(df['Science_Score'].mean(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

numeric_cols = ['Math_Score', 'Science_Score', 'English_Score', 'Attendance_Percent']
z_scores = np.abs(stats.zscore(df[numeric_cols]))
df_no_outliers = df[(z_scores < 3).all(axis=1)]

print("\nAfter Removing Outliers:")
print(df_no_outliers)

df_no_outliers['Log_English_Score'] = np.log1p(df_no_outliers['English_Score'])

print("\nAfter Log Transformation on English_Score:")
print(df_no_outliers[['English_Score', 'Log_English_Score']])
