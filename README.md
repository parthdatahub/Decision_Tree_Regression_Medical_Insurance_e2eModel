# ML_Regression_Models_Playground
Welcome to the MY ML_Regression_Models repository! This repository is dedicated to exploring and showcasing various machine learning regression models. From simple linear regression to advanced techniques like random forest and gradient boosting, this repository provides a comprehensive collection of regression models implemented in Python.

# Medical Insurance Premium Prediction using Decision Tree Regression
This project aims to predict the charges required for medical insurance using a Decision Tree regression model. The model is trained on a dataset of medical insurance records and uses various features to make accurate predictions.

# Problem Statement
The goal of this project is to develop a predictive model that can estimate the charges required for medical insurance based on input variables such as age, BMI, smoking status, etc. The decision tree regression algorithm is utilized for this purpose.

# Dataset
The dataset used for this project contains information about individuals' medical insurance records, including attributes such as age, BMI, number of children, smoking status, region, and charges. The dataset is available in : https://www.kaggle.com/datasets/datalinkparth/medical-insurance-regression

# Model Training
The decision tree regression algorithm is used to train the predictive model. The following steps were followed during the training process:

Data preprocessing: The dataset was cleaned and prepared for training, including handling missing values, encoding categorical variables, and scaling numerical features if necessary.

Splitting the data: The dataset was split into training and testing sets to evaluate the model's performance. A common split ratio, such as 80:20 or 70:30, was used.

Model training: The decision tree regression model was trained using the training data. The algorithm learned the underlying patterns and relationships between the input features and the target variable (medical insurance charges).

Model evaluation: The trained model was evaluated using the testing data to assess its performance. The accuracy metric was used to measure the model's predictive ability. After cross-validation and pruning, the accuracy achieved was as follows:

Training accuracy: 85.92%
Testing accuracy: 84.96%

# Results and Visualizations
To gain insights into the decision-making process of the trained decision tree model, screenshots of the generated decision trees were included in this project. The screenshots visually represent the splits and decisions made by the model.

# Usage
To run the project and reproduce the results, follow these steps:
1. Clone the repository: 
> Clone the repository:

2. Execute the main script:
> python main.py

# Conclusion
In this project, we developed a decision tree regression model to predict medical insurance charges. The model achieved promising accuracy after cross-validation and pruning. By using this model, insurance companies and individuals can estimate the charges for medical insurance based on various factors, facilitating informed decision-making.

Feel free to customize the README.md file according to your project's specific details and requirements.
