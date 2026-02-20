# 🌾 Agricultural Crop Yield Predictor

## 📌 Project Overview
This project is an interactive Machine Learning web application designed to predict the yield of various crops (in tons per hectare). By analyzing environmental factors like temperature, rainfall, soil type, and farming parameters, this tool demonstrates how data science can be applied to precision agriculture to optimize harvests and ensure food security.

## ⚙️ Tech Stack
* **Machine Learning:** Scikit-Learn, XGBoost
* **Data Manipulation:** Pandas, NumPy
* **Web Deployment:** Streamlit
* **Model Serialization:** Joblib

## 🚀 Live Demo
Check out the live web application here: **[https://crop-yield-predictor-k2.streamlit.app/]**

## 📊 Dataset
Kaggle Dataaset: **[https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield]**

## 🧠 How It Works
The core of this application is an **XGBoost Regressor**, trained on a large dataset of agricultural metrics. 
1. **Preprocessing:** Categorical data (like Soil Type and Region) are transformed using One-Hot Encoding. Boolean values (Fertilizer/Irrigation usage) are mapped to integers.
2. **Prediction Pipeline:** The user inputs custom parameters via the Streamlit interface. The app automatically aligns these inputs with the model's training structure (handling missing categories dynamically via reindexing) to generate an accurate yield prediction in real-time.

## 📂 Repository Structure
* `app.py`: The Streamlit web application script.
* `crop_yield.ipynb`: The Jupyter Notebook containing the Exploratory Data Analysis (EDA), feature engineering, and XGBoost model training.
* `crop_yield_model.pkl`: The serialized XGBoost regression model.
* `model_columns.pkl`: The saved feature columns ensuring input alignment.
* `requirements.txt`: The dependencies required to run the app.

## 💻 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`


## ⚠️ Model Limitations & Real-World Applicability
While this model achieves high accuracy on the provided dataset, it is important to note its limitations if applied to real-world agricultural environments:

* **Synthetic/Simplified Data:** The dataset uses broad, generalized categories. For instance, `Fertilizer_Used` is a simple True/False boolean. In reality, crop yield heavily depends on the *exact composition* (NPK ratio) and *quantity* of the fertilizer applied.
* **Missing Micro-climate Variables:** The model relies on average temperature and rainfall. It does not account for hyper-local extreme weather events (e.g., a single day of unexpected frost, hail, or severe drought) which can decimate a yield despite good average conditions.
* **Biological Factors Excluded:** Crucial biological elements such as pest infestations, weed competition, seed variety genetics, and soil nutrient depletion over time are not captured in this dataset.

**Future Improvements:** To make this model production-ready for commercial farming, the dataset would need to be enriched with satellite imagery (for precise weather/soil moisture tracking), IoT sensor data from tractors, and specific chemical soil analyses.
