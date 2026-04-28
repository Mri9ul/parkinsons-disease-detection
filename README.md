# 🧠 Parkinson’s Disease Detection

This project uses machine learning to detect **Parkinson’s disease** based on biomedical voice measurements.

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and should **NOT** be used for real medical diagnosis.

---

## 📌 Objective

The objective of this project is to:

* Build a classification model to detect Parkinson’s disease
* Analyze biomedical voice features
* Compare machine learning models
* Provide predictions through a simple Streamlit web application

---

## 📊 Dataset

The dataset contains **195 records** with biomedical voice measurements.

### Features include:

* Fundamental frequency (Fo, Fhi, Flo)
* Jitter and Shimmer measurements
* Noise-to-harmonics ratio (NHR)
* Harmonics-to-noise ratio (HNR)
* Nonlinear dynamical complexity measures

### Target Variable:

* **1 → Parkinson’s Disease Detected**
* **0 → No Parkinson’s Disease**

---

## ⚙️ Project Workflow

1. Data loading
2. Data preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature scaling using StandardScaler
5. Train-test split (with stratification)
6. Model training:

   * Linear SVM
   * RBF SVM
7. Model evaluation
8. Model comparison
9. Final model selection
10. Model saving
11. Streamlit app development

---

## 🧠 Models Used

* **Linear Support Vector Machine (SVM)**
* **RBF Kernel SVM**

---

## 📈 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🏆 Results

* Linear SVM achieved the best performance
* Final model achieved approximately:
---

## 💡 Key Insights

* The dataset is imbalanced, with more Parkinson’s cases than non-Parkinson’s
* Feature scaling significantly improves SVM performance
* SVM performs well for high-dimensional biomedical data

---

## 🖥️ Streamlit App

A Streamlit web app is included.

### Features:

* Upload CSV file
* Model predicts Parkinson’s disease detection
* Displays results instantly
* Download predictions as CSV

---

## ▶️ Usage

1. Run the notebook to understand the model
2. Run the Streamlit app for predictions

---


