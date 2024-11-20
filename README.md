# **MSDS 570: Final Project**  
**Investigating the Relationship Between Sensory Symptoms and Migraine Intensity**  

## **Table of Contents**

1. [Project Overview](#project-overview)  
2. [Dataset Description](#dataset-description)
3. [Project Objectives](#project-objectives)  
4. [Expected Outcomes](#expected-outcomes)  
5. [Repository Structure](#repository-structure)  
6. [Methodology](#methodology)  
7. [Installation and Usage](#installation-and-usage)  
   - [Setup Instructions](#setup-instructions)  
   - [Running Jupyter Notebooks](#running-jupyter-notebooks)  
   - [Running the Dash App](#running-the-dash-app)  
8. [Dependencies](#dependencies)  
9. [Acknowledgments](#acknowledgments)

---

## **Project Overview**
Understanding the relationship between sensory symptoms and migraine intensity is crucial for identifying potential triggers and improving migraine management strategies. This project leverages data visualization techniques to uncover trends and insights that might otherwise go unnoticed.

---

## **Dataset Description**
- **Source**: [Migraine Dataset on Kaggle](https://www.kaggle.com/datasets/ranzeet013/migraine-dataset)  
- **Number of Records**: 400  
- **Number of Attributes**: 24  
- **Highlights**: The dataset contains sensory symptoms, migraine intensity, migraine characteristics, and patient demographics.  

For a complete description of the attributes, refer to the [source materials](https://codeocean.com/capsule/1269964/tree/v1).

---

## **Project Objectives**
1. Analyze correlations between sensory symptoms and the intensity/duration of migraines.  
2. Visualize the distribution and frequency of sensory symptoms across patient demographics and migraine types.  
3. Provide actionable insights through interactive tools for exploring the data.  

---

## **Expected Outcomes**
1. **Interactive Visualizations**:
   - Heatmaps, scatter plots, box plots, and stacked bar charts to display trends and correlations.  
2. **Dash App**:
   - An interactive dashboard allowing users to explore and manipulate the data.  
3. **Insights**:
   - Highlights potential migraine triggers and symptom patterns for actionable recommendations.  

---

## **Repository Structure**
```
├── README.md                     # Overview of the project
├── data/                         # Dataset and related files
│   └── migraine_dataset.csv      # The dataset
├── notebooks/                    # Jupyter notebooks
│   ├── 01_data_preprocessing.ipynb  # Preprocessing and cleaning
│   ├── 02_exploratory_analysis.ipynb # Visualizations and trends
├── scripts/                      # Python scripts
│   ├── preprocess.py             # Data preparation functions
│   ├── visualize.py              # Functions for creating visualizations
│   ├── app.py                    # Dash app for interactive exploration
├── results/                      # Outputs (plots, dashboards, etc.)
│   ├── visualizations/           # Generated visualizations
├── requirements.txt              # Dependencies and libraries
└── LICENSE                       # License information
```

---

## **Methodology**
1. **Data Preprocessing**:
   - Clean and encode the dataset.
   - Handle categorical variables where necessary.  
2. **Exploratory Data Analysis**:
   - Generate visualizations to identify trends and correlations.  
3. **Interactive Dashboard**:
   - Build a Plotly Dash application to allow users to interact with the data.

---

## **Installation and Usage**

### **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/dpounds24/MSDS-570-FinalProject.git
   ```
2. Navigate to the project folder:
   ```bash
   cd MSDS-570-FinalProject
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Running Jupyter Notebooks**
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open and run the notebooks in the `notebooks/` folder.

### **Running the Dash App**
1. Navigate to the `scripts/` directory:
   ```bash
   cd scripts
   ```
2. Run the Dash application:
   ```bash
   python app.py
   ```
3. Access the app at `http://localhost:8050`.

---

## **Dependencies**
The project requires the following Python libraries:
```
pandas
numpy
plotly
dash
matplotlib
seaborn
jupyter
```

---

## **Acknowledgments**
- **Kaggle**: For providing the [Migraine Dataset](https://www.kaggle.com/datasets/ranzeet013/migraine-dataset).  
- **Dr. Qian**: For guidance throughout this project.  
- **Meharry Medical College**: For supporting this educational endeavor.

---
