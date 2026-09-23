# 🌬️ Wind Turbine Active Power Prediction

An end-to-end **Machine Learning project** designed to predict the **active power output of a wind turbine** using a specified date and time.

The project covers the complete machine learning pipeline, including **data preprocessing, timestamp-based feature engineering, model development using XGBoost, performance evaluation, and deployment through a Flask web application on Render**.

## 🚀 Live Demo

🔗 **Live Application:**
https://turbine-power-prediction.onrender.com/

## 📌 Project Overview

Wind turbine power generation can vary significantly depending on operating conditions and time-related patterns. This project uses historical wind turbine data to develop a machine learning model that predicts the expected **active power generation** for a user-provided date and time.

The trained model is integrated into a **Flask web application**, allowing users to enter a date and time through a simple interface and obtain the predicted turbine power output instantly.

## 🎯 Project Objectives

* Study and analyze historical wind turbine power-generation data
* Preprocess the available dataset for machine learning
* Extract useful information from timestamp data
* Create time-based features for improved prediction
* Develop an XGBoost regression model
* Measure the performance of the trained model using suitable regression metrics
* Store the trained model using Pickle for later use
* Develop a web-based prediction interface using Flask
* Deploy the completed application online using Render

## 🧠 Machine Learning Methodology

### Feature Engineering

The original timestamp information is transformed into several useful features that help the machine learning model identify time-dependent patterns in wind turbine power generation.

The extracted features include:

* **Hour**
* **Minute**
* **Day**
* **Month**
* **Year**
* **Day of Week**
* **Day of Year**

These features enable the model to capture variations and recurring patterns in turbine power output across different hours, days, months, and years.

### 🤖 Machine Learning Model

The project uses the **XGBoost Regressor**, a gradient-boosting algorithm suitable for regression problems and capable of learning complex relationships within the dataset.

The primary model parameters include:

```python
n_estimators = 1000
learning_rate = 0.01
```

The trained model is then saved using **Pickle** and loaded by the Flask application whenever a prediction is requested.

## 🌐 Web Application

A **Flask-based web interface** is used to connect the machine learning model with the user.

The workflow is:

**User enters Date & Time → Features are extracted → XGBoost Model processes the input → Predicted Active Power is displayed**

## ☁️ Deployment

The Flask application is deployed on **Render**, making the turbine power prediction system accessible through a web browser without requiring the user to run the machine learning code locally.

