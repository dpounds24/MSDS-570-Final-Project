import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

def plot_missing_data(data):
    msno.bar(data)
    plt.show()

def plot_variable_distributions(data):
    plt.figure(figsize=(35, 30))
    columns = list(data.columns)
    for i, column in enumerate(columns[:24]):
        plt.subplot(6, 4, i+1)
        sns.histplot(data[column]) if data[column].dtype != 'object' else sns.countplot(x=column, data=data)
        plt.title(f"Distribution of {column}")
    plt.tight_layout()
    plt.show()

def calculate_summary_statistics(data, columns):
    mean_values = data[columns].mean()
    median_values = data[columns].median()
    mode_values = data[columns].mode().iloc[0]
    min_values = data[columns].min()
    max_values = data[columns].max()
    range_values = max_values - min_values
    variance_values = data[columns].var()
    summary_stats = pd.DataFrame({
        'Mean': mean_values,
        'Median': median_values,
        'Mode': mode_values,
        'Min': min_values,
        'Max': max_values,
        'Range': range_values,
        'Variance': variance_values
    })
    return summary_stats
