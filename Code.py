import pandas as pd
import seaborn as sns
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv("nonparametric_data.csv")

# Extract the values for each group
group1 = data[data["Group"] == "Group 1"]["Value"]
group2 = data[data["Group"] == "Group 2"]["Value"]

# Perform the Mann-Whitney U test
result = mannwhitneyu(group1, group2)

# Print the test statistic and p-value
print("Test Statistic:", result.statistic)
print("P-value:", result.pvalue)

# Visualize the distributions using a box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x=data["Group"], y=data["Value"])
plt.xlabel("Group")
plt.ylabel("Value")
plt.title("Comparison of Group Distributions")
plt.show()
