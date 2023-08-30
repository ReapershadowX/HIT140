## TEAM MEMBERS ##
## SUBODH GAUTAM - S372144 ##
## LIKHON KUMAR MITRA - S372288 ##
## MANJIL BOLAKHE - S371743 ##
## SAYEM ALVI - S371489 ##



import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Define custom column names
column_names = [
    
    'Subject identifier', 'Jitter %', 'Jitter absolute', 'Jitter rap', 'Jitter ppq5', 'Jitter ddp',
    'Shimmer %', 'Shimmer absolute', 'Shimmer apq3', 'Shimmer apq5', 'Shimmer apq11', 'Shimmer dda',
    'Harmonicity autocorrelation', 'Harmonicity NHR', 'Harmonicity HNR',
    'Pitch median', 'Pitch mean', 'Pitch standard deviation', 'Pitch minimum', 'Pitch maximum',
    'Pulse number of pulses', 'Pulse number of periods', 'Pulse mean period', 'Pulse standard deviation', 
    'Voice fraction of unvoiced frames', 'Voice number of voice breaks', 'Voice degree of voice breaks',
    'UPDRS', 'PD indicator'
]

# Load the dataset 
data = pd.read_csv('po1_data.csv', header=None, names=column_names)

# Separate the data into PD and healthy groups
pd_group = data[data['PD indicator'] == 1]
healthy_group = data[data['PD indicator'] == 0]

# List of all variables in the dataset
all_variables = [
    'Jitter %', 'Jitter absolute', 'Jitter rap', 'Jitter ppq5', 'Jitter ddp',
    'Shimmer %', 'Shimmer absolute', 'Shimmer apq3', 'Shimmer apq5', 'Shimmer apq11', 'Shimmer dda',
    'Harmonicity autocorrelation', 'Harmonicity NHR', 'Harmonicity HNR',
    'Pitch median', 'Pitch mean', 'Pitch standard deviation', 'Pitch minimum', 'Pitch maximum',
    'Pulse number of pulses', 'Pulse number of periods', 'Pulse mean period', 'Pulse standard deviation', 
    'Voice fraction of unvoiced frames', 'Voice number of voice breaks', 'Voice degree of voice breaks',
    'UPDRS'
]

# List to store significant and non-significant variables
significant_variables = []
non_significant_variables = []

# Descriptive Statistics
print("Descriptive Statistics:")
for variable in all_variables:
    pd_values = pd_group[variable]
    healthy_values = healthy_group[variable]
    
    # Calculate mean, median, and standard deviation
    pd_mean = pd_values.mean()
    healthy_mean = healthy_values.mean()
    pd_median = pd_values.median()
    healthy_median = healthy_values.median()
    pd_std = pd_values.std()
    healthy_std = healthy_values.std()
    
    print(f"Variable: {variable}")
    print(f"PD Group: Mean = {pd_mean:.4f},Median = {pd_median:.4f}, Std Dev = {pd_std:.4f}")
    print(f"Healthy Group: Mean = {healthy_mean:.4f}, Median = {healthy_median:.4f}, Std Dev = {healthy_std:.4f}")
    print()

# Hypotheses Testing
print("Inferential Statistics:  ")
print("Hypotheses Testing:")
for variable in all_variables:
    pd_values = pd_group[variable]
    healthy_values = healthy_group[variable]
    
    # Perform t-test
    t_stat, p_value = ttest_ind(pd_values, healthy_values)
    
    print(f"Variable: {variable}")
    print(f"Null Hypothesis: There is no significant difference in distributions between PD and healthy groups.")
    print(f"Alternative Hypothesis: There is a significant difference in distributions between PD and healthy groups.")
    print(f"p-value: {p_value:.4f}")
    if p_value < 0.05:
        print("Conclusion: We reject the null hypothesis. There is a significant difference.")
        significant_variables.append(variable)
    else:
        print("Conclusion: We fail to reject the null hypothesis. There is no significant difference.")
        non_significant_variables.append(variable)
    print()

# Print significant variables
print("Significant Variables:")
if len(significant_variables) > 0:
    for variable in significant_variables:
        print(f"- {variable}")
else:
    print("No significant variables were found to have an impact in this analysis.")

# Print non-significant variables
print("\nNon-Significant Variables:")
if len(non_significant_variables) > 0:
    for variable in non_significant_variables:
        print(f"- {variable}")
else:
    print("No non-significant variables were found.")

# Perform t-tests and visualize feature distributions
for variable in significant_variables:
    pd_values = pd_group[variable]
    healthy_values = healthy_group[variable]
    
    # Visualizing the distribution of the variable for each significant group
    plt.figure(figsize=(8, 6))
    plt.hist(pd_values, bins=20, color='blue', alpha=0.5, label='PD Group')
    plt.hist(healthy_values, bins=20, color='green', alpha=0.5, label='Healthy Group')
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {variable}')
    plt.legend()
    plt.show()
