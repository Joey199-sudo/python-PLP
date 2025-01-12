import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
iris = sns.load_dataset('iris')

# Display the first few rows to inspect the data
print("First few rows of the dataset:")
print(iris.head())

# Check the structure of the dataset
print("\nDataset information:")
print(iris.info())

# Check for missing values
missing_values = iris.isnull().sum()
print("\nMissing values in the dataset:")
print(missing_values)

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic statistics of the numerical columns:")
print(iris.describe())

# Group by species and compute the mean of numerical columns
grouped_means = iris.groupby('species').mean()
print("\nMean of numerical columns grouped by species:")
print(grouped_means)

# Identify patterns (simple observations)
print("\nObservations:")
print("- Setosa generally has smaller petal lengths and widths compared to other species.")
print("- Virginica tends to have larger sepal lengths on average.")

# Task 3: Data Visualization
# 1. Line chart (using index as a dummy time variable)
plt.figure(figsize=(10, 6))
plt.plot(iris.index, iris['sepal_length'], label='Sepal Length', color='b')
plt.plot(iris.index, iris['petal_length'], label='Petal Length', color='g')
plt.title("Trends in Sepal and Petal Lengths over Time")
plt.xlabel("Index (as time)")
plt.ylabel("Length (cm)")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar chart showing average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal_length', data=iris, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram of petal length
plt.figure(figsize=(8, 5))
plt.hist(iris['petal_length'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.show()

# 4. Scatter plot of sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=iris, palette='deep')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
