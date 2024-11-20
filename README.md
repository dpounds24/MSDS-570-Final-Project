# **MSDS 570: Final Project**  
**Investigating the Relationship Between Sensory Symptoms and Migraine Intensity**  

## **Table of Contents**
1. [Project Overview](#project-overview)  
2. [Dataset Description](#dataset-description)  
3. [Project Objectives](#project-objectives)  
4. [Expected Outcomes](#expected-outcomes)  
5. [Methodology](#methodology)  
6. [Project Requirements](#project-requirements)  
7. [Repository Structure](#repository-structure)  
8. [How to Use](#how-to-use)  
9. [Acknowledgments](#acknowledgments)  

---

## **Project Overview**
This project investigates the relationship between sensory symptoms and migraine intensity using a dataset of 400 patient records. The goal is to understand patterns and correlations that could help identify potential triggers or indicators of severe migraines, as well as visualize these findings interactively.

---

## **Dataset Description**
- **Source:** [Migraine Dataset on Kaggle](https://www.kaggle.com/datasets/ranzeet013/migraine-dataset)  
- **Characteristics:**
  - **Number of Instances:** 400
  - **Number of Attributes:** 24
  - **Associated Tasks:** Classification
  - **Missing Values:** No  
- **Dataset Information:**  
  A medical dataset containing records of patients diagnosed with various migraine pathologies. Features include patient demographics, sensory symptoms, and migraine intensity levels.  
- **Key Features:**
  - **Sensory Symptoms**: Indicators such as visual, sensory, vertigo, and paresthesia.
  - **Migraine Intensity**: Pain intensity levels (None, Mild, Medium, Severe).  
  - **Attributes**: Refer to the dataset's [description](https://www.kaggle.com/datasets/ranzeet013/migraine-dataset) for a full list of features.

---

## **Project Objectives**
1. Analyze the correlation between sensory symptoms and the intensity/duration of migraines.  
2. Visualize the distribution and frequency of sensory symptoms related to migraine severity.  
3. Identify patterns in sensory symptoms that could indicate severe migraines.  

---

## **Expected Outcomes**
1. **Interactive Visualizations:**
   - Heatmaps, scatter plots, box plots, and stacked bar charts to display relationships.  
2. **Plotly Dash Application:**
   - An interactive dashboard to explore the dataset and visualizations.  
3. **Actionable Insights:**
   - Insights into potential triggers or indicators of severe migraines to inform migraine management strategies.  

---

## **Methodology**
1. **Data Preprocessing:**
   - Load and clean the dataset, normalize features, and encode categorical variables.  
2. **Exploratory Data Analysis:**
   - Generate visualizations to understand the dataset, including trends and correlations.  
3. **Modeling:**
   - Apply machine learning algorithms to classify migraine intensity based on symptoms.  
4. **Interactive Dashboard:**
   - Develop a Plotly Dash application to allow users to interact with the data and visualizations.  

---

## **Project Requirements**
- Python 3.8+  
- Required Libraries (to be installed via `requirements.txt`):  
  ```
  pandas
  numpy
  scikit-learn
  plotly
  dash
  matplotlib
  seaborn
  jupyter
  ```
- Additional tools: Jupyter Notebook for data analysis and Dash for the interactive application.

---

## **Repository Structure**
```
├── README.md                     # Project Overview  
├── data/                         # Dataset and related files
│   └── migraine_dataset.csv      # Kaggle dataset  
├── notebooks/                    # Jupyter Notebooks for analysis  
│   ├── 01_data_preprocessing.ipynb  
│   ├── 02_exploratory_analysis.ipynb  
│   ├── 03_modeling.ipynb  
├── scripts/                      # Python scripts for data processing and modeling  
│   ├── preprocess.py  
│   ├── visualize.py  
│   ├── classify.py  
├── results/                      # Output plots and results  
│   ├── visualizations/  
│   ├── metrics.csv  
├── requirements.txt              # Required libraries and dependencies  
└── LICENSE                       # License for the repository  
```

---

## **How to Use**
### **Set Up the Environment**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/MSDS570-FinalProject.git
   ```
2. Navigate to the project folder:
   ```bash
   cd MSDS570-FinalProject
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Run the Notebooks**
1. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Navigate to the `notebooks/` folder and execute the notebooks in sequence:
   - **01_data_preprocessing.ipynb**: Prepares the dataset for analysis.  
   - **02_exploratory_analysis.ipynb**: Explores the data and generates visualizations.  
   - **03_modeling.ipynb**: Builds and evaluates classification models.

### **Run the Dash Application**
1. Navigate to the `scripts/` folder:
   ```bash
   cd scripts
   ```
2. Run the Dash app:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://localhost:8050`.

---

## **Acknowledgments**
- Kaggle for providing the [Migraine Dataset](https://www.kaggle.com/datasets/ranzeet013/migraine-dataset).  
- Dr. [Professor's Name], for their guidance in this course.  
- Meharry Medical College for the educational resources and support.  

---

Let me know if you'd like me to refine this further!
