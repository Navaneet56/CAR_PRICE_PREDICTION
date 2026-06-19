# 🚗 Automotive Market AI Valuation Engine

A premium, end-to-end Machine Learning web application that predicts the resale price of used cars based on their specification profiles and historical metrics. The web application is built using **Streamlit** and utilizes a trained **Linear Regression** model.

🔗 **Live Web Application:** [Deploy Your App on Streamlit Cloud and Paste Your Link Here]

---

## 📐 Project Overview
This project predicts the selling price of used cars based on several structural and history-based parameters. The dataset consists of various factors that determine a car's valuation in the second-hand market, such as its original showroom price, distance covered, transmission setup, and age.

### 📊 Dataset Specifications
The machine learning model is trained on 7 primary structural and categorical characteristics:
* **Year of Manufacture:** The exact year the vehicle was built.
* **Present_Price:** The original showroom price of the car (in Lakhs).
* **Kms_Driven:** Total distance traveled by the car in kilometers.
* **Fuel_Type:** Type of fuel configuration used (Petrol, Diesel, or CNG).
* **Seller_Type:** Retail sales channel (Dealer or Individual).
* **Transmission:** Gearbox transmission type (Manual or Automatic).
* **Owner:** Number of previous owners.

---

## 🛠️ Tech Stack & Workflow
* **Data Analysis & Visualization:** Python, Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning Frame:** Scikit-Learn (Linear Regression & Lasso Regression)
* **Web Dashboard Framework:** Streamlit
* **Model Serialization:** Pickle

### Model Evaluation Results
* **Linear Regression (Training R² Score):** `~0.8636`
* **Linear Regression (Testing R² Score):** `~0.8366`

---

## 📁 Repository Structure
```text
├── CAR_PRICE_PREDICTION.ipynb   # Jupyter Notebook containing Data Analysis & Model Training
├── app_car.py                  # Main standalone styled Streamlit web application file
├── car_price_model.pkl         # Trained and serialized Linear Regression model artifact
└── requirements.txt            # Python dependencies file for deployment server mapping
