# 🏠🏢 Real Estate Prediction Model

<p align="center">
  <img src="./images/math_lady.jpg" style="max-width: 60%; height: auto;">
</p>


## Project Overview
🎯 **Objective:** Predict real estate prices using various machine learning techniques.

📊 **Data Source:** 
Cleaned real estate dataset with various features.

🔧 **Techniques Used:**
- Data Cleaning
- Feature Encoding
- Imputation of Missing Values
- Model Training & Evaluation


## 📦 Installation

- To run these scripts, you'll need the following Python packages:

- 🌐 `numpy`

- ➕ `matplotlib`

- 🐼 `pandas`

- 🐍 `tqdm`

- 📖 `scikit-learn`

- 🐈 `catboost`

## Workflow

The project workflow consists of the following steps:

1. **Data Preparation**
   - 🧹 **Data Cleaning:** Dropped irrelevant columns and handled missing values.
   - 🏷️ **Feature Encoding:** Transformed categorical variables using OneHotEncoder.
   - 🔄 **Imputation:** Applied KNN Imputation to handle missing values.



2. **Model Training**

   - 🧪 Split the dataset into training and test sets (80% train, 20% test).
   - 📈 Trained a CatBoostRegressor model on the training set.


3. **Model Evaluation**
   - 🧮 Evaluated the model using various performance metrics.
   - 🎯 Fine-tuned the model based on evaluation results.


## Data Preparation
The data cleaning process involved:
- 🗑️ Dropping irrelevant columns such as `Country`, `Fireplace`, `Monthlycharges`, `Locality`, `Propertyid`, `Constructionyear`, `Furnished`, and `Roomcount`.
- 🔄 Encoding categorical features (`District`, `Floodingzone`, `Subtypeofproperty`, `Typeofsale`, `PEB`, `Province`, `Region`) using OneHotEncoder.
- 🔧 Imputing missing values using KNNImputer.

## Model Training
The CatBoostRegressor model was trained on the processed dataset. The training process involved:
- 📊 Splitting the data into training and test sets.
- 🔄 Imputing missing values in the training and test sets.
- 🔍 Performing Grid Search to find the best hyperparameters.

## Model Evaluation
The model was evaluated using the following metrics:
- 📏 **Mean Absolute Error (MAE)**
- 📏 **Root Mean Squared Error (RMSE)**
- 📏 **R^2 Score**

**Best Model Parameters:**


- n_estimators: 1952
- learning_rate:0.09958080678882802
- depth: 10
- learning_rate: [0.001, 0.01, 0.05],
- subsample: 0.9024150233634263
- colsample_bylevel: 0.26048065199333004
- min_data_in_leaf: 24


## Results

The model demonstrated high performance with low error metrics:

- 📏 MAE: 41157.15622697452
- 📏 RMSE: 64824.006407226974
- 📈 R^2 Score: 0.8774760322896411

## Conclusion & Future Work
The CatBoostRegressor model successfully predicts real estate prices with high accuracy. Future work will focus on:
- 🔍 Exploring additional feature engineering techniques.
- 🧪 Testing other regression algorithms.
- 🚀 Deploying the model for real-world applications.

## 👥 Contributor

- 👨‍🦰 Ben Ozfirat


## 📅 Timeline

- `Day 1`: Project setup and Data Cleaning.

- `Day 2`: Feature Encoding and KNN Imputation.

- `Day 3`: Model Training

- `Day 4`: Model Evaluation.

