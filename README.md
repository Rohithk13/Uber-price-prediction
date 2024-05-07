## Introduction
The "Uber Price Prediction" project is an in-depth analytical approach aimed at understanding and predicting Uber fares using New York City's Taxi & Limousine Commission (NYC TLC) data. This project is crucial for various stakeholders, including passengers planning their travel budgets, drivers anticipating earnings, and businesses analyzing transportation costs.

### Problem Statement
Transportation fares, particularly in bustling metropolises like New York City, can vary significantly due to numerous factors such as demand, traffic conditions, time of day, and day of the week. In this project, we seek to address several critical questions:

1. Fare Determination: What are the primary factors influencing Uber fares in NYC? This involves a comprehensive analysis of various elements like travel distance, time, pickup and dropoff locations.

2. Temporal Impact: How do Uber fares vary between weekdays and weekends? This part of the research focuses on identifying patterns and differences in pricing strategies during different days, which can help in optimizing travel plans and operations.

3. Technological Enhancement: How can deep learning techniques enhance the accuracy of fare predictions? By leveraging advanced machine learning models, the project aims to improve predictive performance, providing more precise fare estimates that can benefit all users of the service.

Through this project, we aim to provide a robust model that not only predicts fares accurately but also offers insights into the dynamics of urban transportation pricing. This can empower users with better decision-making tools and potentially drive improvements in service offerings.

## Library Importation
The notebook starts by importing essential Python libraries:
Pandas and Numpy for data manipulation.
PyArrow for handling Parquet files, which are used because they provide efficient data storage and retrieval.
Seaborn and Matplotlib for data visualization, crucial for understanding data distributions and results visually.
Scikit-learn modules for machine learning, including tools for splitting data into training and testing sets, model training, and evaluating model performance.

## Data Loading
The notebook effectively manages the loading of substantial datasets from multiple sources:

### Parquet Files 
 The data spanning from December 2023 to October 2023 is meticulously stored in Parquet format, a choice driven by Parquet's efficiency in handling large datasets. The specified files are loaded into separate DataFrames. Each of these files contains a comprehensive dataset, with the combined dataset encompassing approximately 1.8 million rows and a total size nearing 1.5 GB. This extensive dataset ensures a robust foundation for our analysis.

### Concatenation
 After individual loading, all the DataFrames are concatenated into a singular DataFrame named merged_df. This concatenation facilitates a unified platform for subsequent analysis and modeling, ensuring that insights derived are reflective of comprehensive data rather than isolated segments.


##  Data Overview and Inspection
After loading the data, the notebook proceeds to inspect it:

Shape of DataFrame: merged_df.shape is used to view the number of rows and columns, giving an idea of the dataset's size.
Data Types: merged_df.dtypes checks the types of each column to ensure correct data handling, especially before any processing or modeling.
DataFrame Info: merged_df.info() provides a summary, including index dtype and columns, non-null values, and memory usage. This is useful for identifying missing data and understanding the DataFrame's structure.

##  Further Data Processing and Analysis
While not detailed in the summary, typical next steps would include:

Data Cleaning: Handling missing values, correcting data types if necessary, and removing or filling null values.

### Exploratory Data Analysis (EDA)
Our exploratory data analysis is pivotal in uncovering the underlying patterns and distributions within the data, which can influence fare predictions. Key highlights include:

#### Visual Analysis
Box Plot of Trip Miles: We utilized box plots to visualize the distribution of trip distances (measured in miles) among Uber rides. The box plot for the trip_miles variable (shown in the project repository) clearly indicates the central tendency, dispersion, and presence of outliers which can affect fare calculations. This visualization helps in identifying trips that are unusually long or short compared to typical rides.
![image](https://github.com/Rohithk13/UBER_Trip_Price_Prediction/assets/144849666/97d6b53f-03db-43b1-ae77-de287cff14dd)

Histograms: Histograms were employed to analyze the frequency distribution of various continuous variables such as fare amounts and ride durations. These histograms help in understanding the skewness of the data and identifying the most common values within a dataset. For example, the histogram of fare_amounts helped us observe that the majority of fares fall within a particular range, highlighting the typical cost passengers can expect for their rides. Additionally, the distribution provides insights into the prevalence of higher or lower fare outliers, which could be influenced by factors such as trip length, time of day, or special events.
![image](https://github.com/Rohithk13/UBER_Trip_Price_Prediction/assets/144849666/5f24ebe8-b6d3-400a-9ee3-aa6165444e00)

By thoroughly examining these visual representations, we gain a detailed understanding of the factors that most significantly impact Uber fares and can better tailor our predictive models to reflect these insights.

### Feature Engineering
In our pursuit to build an effective predictive model, feature engineering played a critical role in enhancing the input dataset by introducing new, meaningful features derived from existing data. These transformations are key in improving model accuracy by providing additional context that the model can learn from.
Newly Added Features
Pickup Hour: We extracted the hour of the day from the pickup timestamp. This feature, pickup_hour, is crucial as fare rates can vary significantly throughout the day due to factors like rush hours, nighttime rates, and general traffic patterns.
Day of the Week: We converted the pickup date into a day of the week with a numerical format, where Monday is represented as 0 and Sunday as 6. The feature, pickup_day, helps the model capture weekly patterns, such as the difference in fare prices and ride frequency between weekdays and weekends.

# Methodology
Our approach to predicting Uber fares involves several advanced machine learning techniques and algorithms. Each chosen method was aimed at optimizing the prediction accuracy by leveraging different aspects of our data.

### Algorithms Used
Linear Regression: Served as a baseline model, providing a quick and straightforward understanding of the relationship between independent variables and the fare.

Decision Tree Regressor: A more complex model that captures non-linear relationships more effectively than linear regression. It was especially useful for handling categorical data without extensive preprocessing.

XGBoost Regressor: Known for its performance and speed, this advanced gradient boosting model was used for its ability to handle large datasets efficiently and with high accuracy.

Fully Connected Neural Network: As a deep learning approach, this model was designed to capture intricate patterns in the data that simpler models might miss, using multiple layers of neurons.
Hyperparameter Tuning
Hyperparameter tuning was conducted for both the Decision Tree and XGBoost regressors to optimize their configurations:

Decision Tree Regressor: We experimented with different tree depths to prevent overfitting while maximizing the prediction accuracy.

XGBoost Regressor: Tuning involved adjusting parameters like learning rate, number of estimators, and tree depth across 10, 15, and 25 epochs to find the optimal setting that balances training speed and model performance.
Model Evaluation and Selection
After training, each model was evaluated based on its accuracy and R² (coefficient of determination) value. The XGBoost regressor emerged as the top-performing model with the highest accuracy and the best R² value, indicating its superior ability to predict Uber fares accurately compared to other models.

# Model Deployment with Streamlit on Streamlit Public Cloud
In this repository, we demonstrate the deployment of an XGBoost model using Streamlit, a popular Python library for building interactive web applications, and hosting it on Streamlit Public Cloud.

### Steps to Deploy the Model
1. Export the XGBoost Model
We first export our trained XGBoost model into a pickle file named xgb_classifier.pkl. This file contains the serialized version of our model, ready for deployment.

2. Create the Streamlit UI
We develop the user interface for our model using Streamlit in a Python script named app1.py. This script defines the input parameters that the model expects from the user and generates the model output accordingly.

3. Set Up GitHub Repository
We create a GitHub repository to manage our code and files related to the deployment process. This repository serves as the central hub for version control and collaboration.

4. Connect GitHub Repo to Streamlit Public Cloud
We connect our GitHub repository to Streamlit's public cloud platform. This integration allows us to deploy our Streamlit application directly from our GitHub repository.

5. Deploy Model on Streamlit Public Cloud
We deploy our Streamlit application, along with our XGBoost model, on Streamlit Public Cloud. The deployment process is seamless, and our application becomes accessible via a public URL.

## Usage
To use the deployed model:

Visit the deployed Streamlit application URL.
https://ubertrippriceprediction-exc9yj5crrcndzkeyvefyj.streamlit.app/ 

Input the required parameters as prompted by the user interface.
Click on the relevant buttons or interact with the interface elements to generate model predictions.
View the model output displayed on the Streamlit UI.
![image](https://github.com/Rohithk13/UBER_Trip_Price_Prediction/assets/144849666/6e197d96-417a-4537-b765-57fee4f53e64)

7. Conclusions and Possible Extensions
This section would likely draw conclusions from the modeling and suggest ways to improve or extend the analysis, perhaps by incorporating additional data or trying different modeling techniques.

