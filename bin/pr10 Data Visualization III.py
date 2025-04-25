import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv(url, names=columns)

# 1. List down the features and their types
features_types = df.dtypes
print("Features and their types:\n", features_types)

# 2. Create a histogram for each feature
df.drop("species", axis=1).hist(figsize=(10, 8))
plt.suptitle('Histogram of Features')
plt.show()

# 3. Create a boxplot for each feature
sns.boxplot(data=df.drop("species", axis=1), orient="h", palette="Set2")
plt.title('Boxplot of Features')
plt.show()

# 4. Compare distributions and identify outliers
sns.pairplot(df, hue="species", palette="Set1")
plt.suptitle('Pairplot of Features with Species', y=1.02)
plt.show()
