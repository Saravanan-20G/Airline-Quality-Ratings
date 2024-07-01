# Airline Customer Satisfaction Prediction App
This Streamlit app predicts airline customer satisfaction based on user inputs. The app uses a pre-trained machine learning model to make predictions.
## Features
User-friendly Interface: Input features via a form.

Machine Learning Model: Predicts customer satisfaction using a Random Forest classifier.

Real-time Predictions: Provides instant predictions based on user inputs

## Dataset
The dataset used in this project contains features related to airline customer satisfaction, including:
```ID
Gender
Age
Flight Distance
Departure Delay
Arrival Delay
Customer Type
Type of Travel
Class
Satisfaction (Target Variable)```


## Steps Performed
Data Loading and Preprocessing:

Loaded the dataset.
Checked for missing values and filled missing 'Arrival Delay' values with 0.
Identified continuous and categorical columns.
Encoded the 'Satisfaction' column using Label Encoding.
One-hot encoded the other categorical columns.
Feature Selection and Splitting:

Selected the feature columns and target variable.
Split the data into training and testing sets (80-20 split).
Data Scaling:

Applied StandardScaler to scale the feature columns.
Model Training:

Trained a Random Forest Classifier on the training data.
Model Evaluation:

Evaluated the model using confusion matrix, classification report, and accuracy score.
Performed Grid Search with Cross-Validation to find the best hyperparameters.
Model Saving and Loading:

Saved the best model using Joblib.
Loaded the model for prediction.
Streamlit Deployment:

Created a Streamlit application to take user inputs and predict customer satisfaction.
