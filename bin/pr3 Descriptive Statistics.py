import pandas as pd
import numpy as np
import seaborn as sns

# Part 1: Grouped Summary Statistics
df = sns.load_dataset("titanic")

grouped_stats = df.groupby('class')['age'].agg(['count', 'mean', 'median', 'min', 'max', 'std']).reset_index()
print("Summary Statistics for 'age' grouped by 'class':")
print(grouped_stats)

age_list = df.dropna(subset=['class', 'age']).groupby('class')['age'].apply(list).reset_index()
print("\nList of ages for each class:")
print(age_list)

# Part 2: Iris Dataset Statistics
iris = sns.load_dataset('iris')

setosa = iris[iris['species'] == 'setosa']
versicolor = iris[iris['species'] == 'versicolor']
virginica = iris[iris['species'] == 'virginica']

print("\nSetosa Statistics:")
print(setosa.describe(percentiles=[.25, .5, .75]))

print("\nVersicolor Statistics:")
print(versicolor.describe(percentiles=[.25, .5, .75]))

print("\nVirginica Statistics:")
print(virginica.describe(percentiles=[.25, .5, .75]))
