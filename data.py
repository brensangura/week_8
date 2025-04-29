import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width',
                'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(url, names=column_names)

# Display the first few rows
print("First 5 rows of the dataset:")
print(iris_df.head())

# Explore the structure
print("\nDataset info:")
print(iris_df.info())

# Check for missing values
print("\nMissing values:")
print(iris_df.isnull().sum())

# Clean the dataset (though iris dataset is typically clean)
iris_df_clean = iris_df.dropna()  # In case there were any missing values

# Basic statistics
print("\nBasic statistics:")
print(iris_df_clean.describe())

# Group by species and compute mean measurements
print("\nMean measurements by species:")
print(iris_df_clean.groupby('species').mean())

# Additional interesting analysis
print("\nPetal length statistics by species:")
print(iris_df_clean.groupby('species')[
      'petal_length'].agg(['mean', 'median', 'std']))

plt.figure(figsize=(15, 10))

# 1. Line chart (though time-series isn't applicable, we'll use index as x-axis)
plt.subplot(2, 2, 1)
iris_df_clean['sepal_length'].plot(
    kind='line', title='Sepal Length Trend (by index)')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')

# 2. Bar chart - average petal length by species
plt.subplot(2, 2, 2)
iris_df_clean.groupby('species')['petal_length'].mean().plot(
    kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')

# 3. Histogram - distribution of sepal width
plt.subplot(2, 2, 3)
iris_df_clean['sepal_width'].plot(kind='hist', bins=15, edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')

# 4. Scatter plot - sepal length vs petal length
plt.subplot(2, 2, 4)
colors = {'Iris-setosa': 'red',
          'Iris-versicolor': 'blue', 'Iris-virginica': 'green'}
plt.scatter(iris_df_clean['sepal_length'], iris_df_clean['petal_length'],
            c=iris_df_clean['species'].map(colors))
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=v, label=k)
                    for k, v in colors.items()])

plt.tight_layout()
plt.show()

# Bonus: Pairplot for comprehensive visualization
sns.pairplot(iris_df_clean, hue='species')
plt.suptitle('Pairwise Relationships in Iris Dataset', y=1.02)
plt.show()
