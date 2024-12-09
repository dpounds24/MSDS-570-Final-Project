import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_histogram(data, column, title, bins=10, kde=True):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=data, x=column, bins=bins, kde=kde, color='blue')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

def plot_correlation_heatmap(data, columns):
    correlation_matrix = data[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="viridis")
    plt.title("Correlation Heatmap")
    plt.show()

def plot_3d_scatter(data):
    return px.scatter_3d(
        data,
        x='Duration',
        y='Total_Sensory_Symptoms',
        z='Intensity',
        color='Type',
        title="3D Scatter Plot: Duration vs Sensory Symptoms",
        labels={
            'Duration': 'Migraine Duration',
            'Total_Sensory_Symptoms': 'Total Sensory Symptoms',
            'Intensity': 'Migraine Intensity',
            'Type': 'Migraine Type'
        }
    )
