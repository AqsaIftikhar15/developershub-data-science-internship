# 🏥 Insurance Claim Amount Prediction

## 📌 Objective
The goal of this task is to predict **medical insurance claim charges** based on personal and lifestyle attributes such as age, BMI, smoking status, and region using **Linear Regression**.

---

## 📂 Dataset
**Medical Cost Personal Dataset**

**Features include:**
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region
- Insurance charges (target variable)

---

## 🛠️ Tools & Technologies
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 🔍 Approach
1. Loaded and explored the dataset using Pandas
2. Checked and confirmed absence of missing values
3. Encoded categorical variables (e.g., smoker)
4. Performed Exploratory Data Analysis (EDA):
   - Age vs Charges
   - BMI vs Charges
   - Smoker vs Charges
5. Trained a **Linear Regression** model
6. Evaluated performance using:
   - Mean Absolute Error (MAE)
   - Root Mean Squared Error (RMSE)

---

## 📊 Results
- **MAE:** ~4260  
- **RMSE:** ~5875  

The results show that **smoking status**, **BMI**, and **age** have a significant impact on insurance charges.

---

## 🧠 Key Insights
- Smokers incur substantially higher insurance costs
- Insurance charges increase with age
- Higher BMI is associated with higher medical expenses

---

## ✅ Conclusion
This task demonstrates how regression models can be used to estimate continuous outcomes like insurance costs and highlights the importance of lifestyle factors in healthcare analytics.

---

📁 *This project was completed as part of the DevelopersHub Data Science & Analytics Internship.*
