<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Heart Disease Prediction</title>
</head>
<body>

<h1>❤️ Heart Disease Prediction System</h1>

<p>
A complete <strong>end-to-end Machine Learning pipeline</strong> designed to predict the presence of
heart disease using clinical patient data. The project is modular, extensible, and production-ready,
covering <strong>data preprocessing, model training, evaluation, selection, logging, and Flask deployment</strong>.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
Heart disease remains one of the leading causes of death globally. Early prediction enables timely
medical intervention. This project leverages multiple machine learning classification algorithms
to assist healthcare decision-making.
</p>

<p>
The pipeline is intentionally designed with <strong>optional preprocessing stages</strong> (currently commented
in <code>main.py</code>) to demonstrate real-world ML workflow flexibility.
</p>

<hr>

<h2>📊 Dataset Information</h2>

<ul>
    <li><strong>Dataset:</strong> heart.csv</li>
    <li><strong>Target Variable:</strong></li>
</ul>

<ul>
    <li><strong>1</strong> → Heart Disease Detected</li>
    <li><strong>0</strong> → No Heart Disease</li>
</ul>

<h3>🔍 Feature Description</h3>

<table border="1" cellpadding="6" cellspacing="0">
    <tr>
        <th>Feature</th>
        <th>Description</th>
    </tr>
    <tr><td>age</td><td>Age of the patient</td></tr>
    <tr><td>sex</td><td>Gender (1 = Male, 0 = Female)</td></tr>
    <tr><td>cp</td><td>Chest pain type</td></tr>
    <tr><td>trestbps</td><td>Resting blood pressure</td></tr>
    <tr><td>chol</td><td>Serum cholesterol</td></tr>
    <tr><td>fbs</td><td>Fasting blood sugar</td></tr>
    <tr><td>restecg</td><td>Resting ECG results</td></tr>
    <tr><td>thalach</td><td>Maximum heart rate achieved</td></tr>
    <tr><td>exang</td><td>Exercise induced angina</td></tr>
    <tr><td>oldpeak</td><td>ST depression</td></tr>
    <tr><td>slope</td><td>Slope of peak exercise ST segment</td></tr>
    <tr><td>ca</td><td>Number of major vessels</td></tr>
    <tr><td>thal</td><td>Thalassemia type</td></tr>
</table>

<hr>

<h2>⚙️ Project Architecture</h2>

<pre>
Heart-Disease-Prediction/
│
├── app.py
├── main.py
├── model_training.py
├── data_balance.py
├── missing_val_handle.py
├── variable_transformation_outlierhandle.py
├── log_code.py
├── heart.csv
├── best_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── logs/
    └── *.log
</pre>

<hr>

<h2>🔁 Machine Learning Pipeline (Detailed)</h2>

<h3>1️⃣ Data Loading & Initial Analysis</h3>
<ul>
    <li>Dataset loaded using Pandas</li>
    <li>Shape, data types, and missing values logged</li>
    <li>Independent (X) and target (y) variables separated</li>
</ul>

<h3>2️⃣ Train–Test Split</h3>
<ul>
    <li>80% training data</li>
    <li>20% testing data</li>
    <li>Random state fixed for reproducibility</li>
</ul>

<h3>3️⃣ Missing Value Handling (Optional)</h3>
<p>
Implemented in <code>missing_val_handle.py</code> and available in <code>main.py</code> (currently commented).
</p>
<ul>
    <li>Random sample imputation</li>
    <li>Preserves original data distribution</li>
    <li>Creates replacement columns safely</li>
</ul>

<h3>4️⃣ Outlier Handling & Feature Transformation (Optional)</h3>
<p>
Implemented in <code>variable_transformation_outlierhandle.py</code>.
</p>
<ul>
    <li>IQR-based outlier capping</li>
    <li>Log transformation for skewed features</li>
    <li>KDE and boxplots generated (before & after)</li>
</ul>

<h3>5️⃣ Data Balancing (Optional)</h3>
<p>
Implemented in <code>data_balance.py</code>.
</p>
<ul>
    <li>SMOTE logic included (commented)</li>
    <li>Can be enabled for imbalanced datasets</li>
</ul>

<h3>6️⃣ Feature Scaling (Optional)</h3>
<p>
Implemented in <code>main.py</code> (commented).
</p>
<ul>
    <li>StandardScaler for continuous variables</li>
    <li>Scaler saved as <code>scaler.pkl</code> for inference</li>
</ul>

<h3>7️⃣ Model Training & Evaluation</h3>

<ul>
    <li>K-Nearest Neighbors</li>
    <li>Naive Bayes</li>
    <li>Logistic Regression</li>
    <li>Decision Tree</li>
    <li>Random Forest</li>
    <li>AdaBoost</li>
    <li>Gradient Boosting</li>
    <li>XGBoost</li>
</ul>

<ul>
    <li>Accuracy, Confusion Matrix, Classification Report</li>
    <li>ROC Curve and AUC Score calculated</li>
</ul>

<h3>8️⃣ Best Model Selection</h3>
<ul>
    <li>Model with highest AUC selected</li>
    <li>Best model saved as <code>best_model.pkl</code></li>
</ul>

<hr>

<h2>📈 Evaluation Metrics</h2>
<ul>
    <li>Accuracy</li>
    <li>Confusion Matrix</li>
    <li>Classification Report</li>
    <li>ROC Curve</li>
    <li>AUC Score</li>
</ul>

<hr>

<h2>🧠 Model Deployment (Flask)</h2>

<ul>
    <li>User inputs medical parameters via web UI</li>
    <li>Inputs converted to Pandas DataFrame</li>
    <li>Trained model predicts outcome</li>
    <li>Prediction and probability displayed</li>
</ul>

<p>
<strong>Prediction Output:</strong><br>
❤️ Heart Disease Detected<br>
💚 No Heart Disease
</p>

<hr>

<h2>🎨 Frontend</h2>
<ul>
    <li>HTML + CSS based responsive UI</li>
    <li>Grid-based input layout</li>
    <li>Clean medical-themed design</li>
</ul>

<hr>

<h2>📝 Logging</h2>
<ul>
    <li>Centralized logging system</li>
    <li>Separate logs for each pipeline stage</li>
    <li>Helps debugging, monitoring, and auditability</li>
</ul>

<hr>

<h2>▶️ How to Run the Project</h2>

<h3>1️⃣ Install Dependencies</h3>
<pre>
pip install numpy pandas scikit-learn matplotlib seaborn flask xgboost
</pre>

<h3>2️⃣ Train the Model</h3>
<pre>
python main.py
</pre>

<h3>3️⃣ Run the Web Application</h3>
<pre>
python app.py
</pre>

<h3>4️⃣ Open Browser</h3>
<pre>
http://127.0.0.1:5000/
</pre>

<hr>

<h2>🚀 Key Highlights</h2>
<ul>
    <li>Modular & extensible ML pipeline</li>
    <li>Optional real-world preprocessing stages</li>
    <li>Multiple model comparison</li>
    <li>AUC-based best model selection</li>
    <li>Flask deployment with clean UI</li>
</ul>

<hr>

<h2>📌 Future Enhancements</h2>
<ul>
    <li>Cloud deployment (AWS / Azure / Render)</li>
    <li>Database integration</li>
    <li>Explainable AI (SHAP)</li>
    <li>Automated CI/CD pipeline</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p>
<strong>Bala Venu</strong><br>
Machine Learning & Data Science Enthusiast
</p>

</body>
</html>
