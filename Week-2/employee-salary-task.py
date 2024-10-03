# Step 1: Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the sample Titanic dataset from CSV file
url = "employee-sal-data.csv"  # Use raw string or forward slashes
df = pd.read_csv(url)

# Original dataset
print("Original Dataset:")
print(df)

# Salary Data
salaries = df['PayscaleMinimum']
print(salaries)

# Calculate Mean, Median, Mode
mean_sal = np.mean(salaries)
median_sal = np.median(salaries)
mode_sal = stats.mode(salaries)[0]

print("Mean Sal", mean_sal)
print("Median Sal", median_sal)
print("Mode Sal", mode_sal)


# Analyse Variability
std_dev_sal = np.std(salaries)
print("Standard Deviation", std_dev_sal)

# Visualize Variability: Histogram
plt.figure(figsize=(10, 6))
sns.histplot(salaries, kde=True, bins=30)
plt.axvline(mean_sal, color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(median_sal, color='blue', linestyle='dashed', linewidth=1, label='Median')
plt.legend()
plt.title('Histogram of Employee Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Step 5: Box Plot Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x=salaries)
plt.title('Box Plot of Employee Salaries')
plt.xlabel('Salary')
plt.show()

# Step 6: Group Analysis
# Let's assume we have a 'JobTitle' column to group salaries by job role.
plt.figure(figsize=(12, 8))
sns.barplot(x='Unit', y='PayscaleMinimum', data=df, estimator=np.mean, ci=None)
plt.xticks(rotation=90)
plt.title('Average Salary by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.show()

