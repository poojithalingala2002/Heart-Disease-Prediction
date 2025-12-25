import numpy as np
import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open('best_model.pkl', 'rb'))
# scaler = pickle.load(open('scaler.pkl', 'rb'))

FEATURE_COLUMNS = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak',
    'slope', 'ca', 'thal'
]

# SCALE_COLS = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = [
            float(request.form[col]) for col in FEATURE_COLUMNS
        ]

        input_df = pd.DataFrame([values], columns=FEATURE_COLUMNS)

        # input_df[SCALE_COLS] = scaler.transform(input_df[SCALE_COLS])

        prediction = model.predict(input_df)[0]

        try:
            prob = model.predict_proba(input_df)[0][1]
            prob = round(prob * 100, 2)
        except:
            prob = None

        result = "Heart Disease Detected ❤️" if prediction == 1 else "No Heart Disease 💚"

        return render_template(
            'index.html',
            prediction_text=result,
            probability=prob
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
