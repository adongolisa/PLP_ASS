# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Convert it to a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target column
df['species'] = iris.target

# Display the first few rows of the dataset
print(df.head())

# Explore the structure of the dataset
print(df.dtypes)
print(df.isnull().sum())

# Clean the dataset (if needed)
df = df.dropna()  # Alternatively, you can fill missing values with df.fillna(value)

# Compute basic statistics
print(df.describe())

# Perform groupings and compute mean
group_means = df.groupby('species').mean()
print(group_means)

# Line chart (Note: Iris dataset does not have time-series data, so this is just an illustrative example)
# If you have time-series data, uncomment and use the following:
# df['date'] = pd.date_range(start='1/1/2020', periods=len(df))  # Placeholder dates
# df.set_index('date', inplace=True)
# df['some_value'] = df['sepal length (cm)']  # Example value
# df['some_value'].plot.line(title='Trends Over Time')
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.show()

# Bar chart showing the average petal length per species
group_means['petal length (cm)'].plot.bar(title='Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Histogram of petal length
df['petal length (cm)'].plot.hist(bins=20, title='Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.show()

# Scatter plot to visualize the relationship between sepal length and petal length
df.plot.scatter(x='sepal length (cm)', y='petal length (cm)', title='Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# Scatter plot with Seaborn
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs. Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Error handling for loading dataset
try:
    iris = load_iris()
except Exception as e:
    print(f"An error occurred: {e}")
