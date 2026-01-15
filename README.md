# Titanic Dataset Analysis 🛳️

This project focuses on performing **Exploratory Data Analysis (EDA)** on the Titanic dataset using **Python and Pandas**.  
The analysis helps in understanding the dataset structure, feature types, data quality issues, and its suitability for **Machine Learning models**.

---

## 📌 Dataset Information
- **Dataset Name:** Titanic Dataset
- **File Used:** `train.csv`
- **Total Records:** 891
- **Total Features:** 12
- **Target Variable:** `Survived`

---

## 🎯 Project Objective
The main objective of this project is to:
- Explore and understand the Titanic dataset
- Identify numerical, categorical, ordinal, and binary features
- Detect missing values and data imbalance
- Assess the dataset’s readiness for machine learning applications

---

## 🧠 Analysis Performed

### 1️⃣ Data Loading & Inspection
- Loaded the dataset using Pandas
- Displayed initial and final records to understand structure

### 2️⃣ Feature Classification
Features were manually categorized into:
- Numerical
- Categorical
- Ordinal
- Binary

### 3️⃣ Dataset Overview
- Used `df.info()` to analyze data types and missing values
- Used `df.describe()` for statistical insights

### 4️⃣ Categorical Feature Analysis
- Examined unique values and distributions
- Identified high-cardinality features

### 5️⃣ Target & Input Feature Selection
- Selected **Survived** as the target variable
- Chose appropriate input features for ML modeling

### 6️⃣ Dataset Suitability for ML
- Evaluated dataset size and structure
- Confirmed suitability for traditional ML algorithms

### 7️⃣ Data Quality Observations
- Identified missing values in **Age**, **Cabin**, and **Embarked**
- Observed class imbalance in the target variable
- Highlighted features requiring preprocessing

---

## ⚠️ Data Quality Issues
- **Cabin** column contains a high percentage of missing values
- **Age** column requires imputation
- Class imbalance may affect model performance
- Categorical variables need encoding

---

## 🛠️ Tools & Technologies
- Python
- Pandas
- Git & GitHub

---

## 📂 Project Structure
