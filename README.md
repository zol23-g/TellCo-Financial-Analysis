
# **Telecom User Engagement and Behavior Analysis**

## **Project Overview**

This project aims to analyze the **telecom dataset** to understand customer behavior and engagement patterns based on various metrics such as session frequency, session duration, and total traffic (download + upload). The analysis is divided into two main tasks:

1. **Task 1 - User Overview Analysis**:  
   Focuses on identifying popular handsets, manufacturers, and user behavior based on session data.
   
2. **Task 2 - User Engagement Analysis**:  
   Investigates user engagement levels, applies clustering algorithms, and provides insights for optimizing network resources.

## **Project Goals**

The objectives of this project are:
- To identify key metrics related to user behavior and handset usage.
- To perform clustering to segment users based on engagement levels.
- To provide insights that can help technical and marketing teams allocate resources effectively.

---

<!-- ## **Project Structure**

```
├── data/                     # Directory containing the telecom dataset (raw and cleaned).
│   ├── telecom_data.csv       # Original telecom dataset.
│   ├── cleaned_telecom_data.csv # Cleaned version of the dataset.
├── notebooks/                 # Jupyter notebooks for analysis.
│   ├── Task_1_User_Overview.ipynb # Notebook for Task 1 analysis.
│   ├── Task_2_User_Engagement.ipynb # Notebook for Task 2 analysis.
├── scripts/                   # Python scripts for data cleaning and outlier handling.
│   ├── missing_values_handler.py   # Handles missing values in the dataset.
│   ├── outliers_handler.py         # Handles outliers in the dataset.
├── reports/                   # Reports and presentations.
│   ├── Interim_Presentation.pdf    # Summary presentation for Task 1 and Task 2.
├── README.md                  # Project documentation.
├── requirements.txt           # List of dependencies and libraries.
└── .gitignore                 # Files and directories to ignore in git.
```

--- -->

## **Getting Started**

### **Prerequisites**

Ensure you have the following tools installed on your local machine:
- Python 3.x
- Jupyter Notebook or Jupyter Lab
- Git

### **Python Dependencies**

The required Python libraries for this project are listed in `requirements.txt`. Install them using the following command:

```bash
pip install -r requirements.txt
```

**Key Libraries:**
- `pandas`: Data manipulation and analysis.
- `numpy`: Numerical computations.
- `matplotlib` & `seaborn`: Data visualization.
- `scikit-learn`: Machine learning algorithms (clustering, PCA).
- `SQLAlchemy`: Database connection (optional, if working with PostgreSQL).

---

## **How to Run the Project**

### **Step 1: Data Cleaning**

The raw telecom data contains missing values and outliers that need to be addressed before analysis. Use the scripts provided to handle these issues:

```python
from scripts.missing_values_handler import handle_missing_numerical, handle_missing_categorical
from scripts.outliers_handler import handle_outliers_numerical

# Example: Handling missing values
df = handle_missing_numerical(df, strategy='mean')
df = handle_missing_categorical(df)

# Example: Handling outliers
df = handle_outliers_numerical(df)
```

Alternatively, you can open the `notebooks/Task_1_User_Overview.ipynb` notebook and run the data cleaning cells.

### **Step 2: Task 1 - User Overview Analysis**

1. Open the `Task_1_User_Overview.ipynb` notebook.
2. Run the cells to perform the following:
   - Identify the top 10 handsets and top 3 manufacturers.
   - Aggregate user behavior by session duration, session frequency, and total data.
   - Visualize the results using bar charts, box plots, and scatter plots.

### **Step 3: Task 2 - User Engagement Analysis**

1. Open the `Task_2_User_Engagement.ipynb` notebook.
2. Perform the following analyses:
   - Aggregate metrics like session frequency, duration, and total traffic.
   - Normalize the engagement metrics.
   - Apply K-Means clustering to group users by engagement levels.
   - Analyze the clusters and identify the most engaged users.

### **Step 4: Visualization and Reporting**

- Use the provided visualizations to understand user behavior and engagement.
- You can find a summary of findings in the `reports/Interim_Presentation.pdf`, which includes:
  - Key visualizations (bar plots, scatter plots, correlation heatmaps, PCA).
  - Recommendations for marketing and technical teams.

---

## **Analysis Breakdown**

### **Task 1: User Overview Analysis**
- **Top Handsets & Manufacturers**: Identified the most popular handsets and manufacturers used by customers.
- **User Behavior on Applications**: Aggregated user data based on session frequency, duration, and total traffic.
- **Variable Transformation & Deciles**: Segmented users into deciles based on session duration and analyzed total data per decile.
- **Univariate & Bivariate Analysis**: Explored individual and pairwise relationships between session metrics and application data.

### **Task 2: User Engagement Analysis**
- **Engagement Metrics**: Calculated key metrics for session frequency, session duration, and total traffic.
- **K-Means Clustering**: Classified users into 3 groups based on their engagement levels.
- **Elbow Method**: Determined the optimal number of clusters using the elbow method.
- **Cluster Interpretation**: Provided insights into user groups (high, medium, low engagement) and offered recommendations for targeting resources.

---

## **Results Summary**

- **Top Handsets & Manufacturers**: Marketing efforts should focus on popular handsets and manufacturers.
- **User Engagement**: High-engagement users can be targeted for premium services, while low-engagement users can receive retention offers.
- **Application Insights**: Social media, Google, and YouTube drive significant traffic, suggesting areas for optimizing network resources.

---

## **Future Work**

- **Improved Clustering**: Explore other clustering techniques (e.g., hierarchical clustering) to refine engagement groups.
- **Time-Series Analysis**: Analyze user behavior over time to identify trends in engagement.
- **Predictive Modeling**: Build models to predict churn based on engagement levels.

---

## **Contact Information**

For any questions or issues regarding this project, please contact:

- **Name**: Zelalem Wubet
- **Email**: zelalemwubet93@gmail.com
- **GitHub**: https://github.com/zol23-g

