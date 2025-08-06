from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Charger le modèle
model = joblib.load("model/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])  # Un seul enregistrement à la fois
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]
    return jsonify({
        "prediction": int(prediction),
        "fraud_probability": round(float(proba), 4)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
