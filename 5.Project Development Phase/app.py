from flask import Flask, render_template, request
import numpy as np
import joblib

# ==========================================
# Initialize Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Load Trained Model and Scaler
# ==========================================

model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# Prediction Page
# ==========================================

@app.route("/predict")
def predict():
    return render_template("predict.html")


# ==========================================
# About Page
# ==========================================

@app.route("/about")
def about():
    return render_template("about.html")


# ==========================================
# Prediction Logic
# ==========================================

@app.route("/result", methods=["POST"])
def result():

    try:

        features = [

            float(request.form["MonsoonIntensity"]),
            float(request.form["TopographyDrainage"]),
            float(request.form["RiverManagement"]),
            float(request.form["Deforestation"]),
            float(request.form["Urbanization"]),
            float(request.form["ClimateChange"]),
            float(request.form["DamsQuality"]),
            float(request.form["Siltation"]),
            float(request.form["AgriculturalPractices"]),
            float(request.form["Encroachments"]),
            float(request.form["IneffectiveDisasterPreparedness"]),
            float(request.form["DrainageSystems"]),
            float(request.form["CoastalVulnerability"]),
            float(request.form["Landslides"]),
            float(request.form["Watersheds"]),
            float(request.form["DeterioratingInfrastructure"]),
            float(request.form["PopulationScore"]),
            float(request.form["WetlandLoss"]),
            float(request.form["InadequatePlanning"]),
            float(request.form["PoliticalFactors"])

        ]

        features = np.array(features).reshape(1, -1)

        scaled = scaler.transform(features)

        prediction = model.predict(scaled)[0]

        probability = round(prediction * 100, 2)

        if probability < 35:
            risk = "LOW"
            color = "success"
            recommendation = [
                "Flood risk is minimal.",
                "Continue monitoring weather updates.",
                "Maintain normal precautions."
            ]

        elif probability < 70:
            risk = "MODERATE"
            color = "warning"
            recommendation = [
                "Stay alert for weather warnings.",
                "Avoid unnecessary travel.",
                "Prepare emergency supplies."
            ]

        else:
            risk = "HIGH"
            color = "danger"
            recommendation = [
                "Follow evacuation instructions.",
                "Avoid flood-prone areas.",
                "Keep emergency contacts ready.",
                "Monitor official alerts continuously."
            ]

        return render_template(
            "result.html",
            probability=probability,
            risk=risk,
            color=color,
            recommendation=recommendation
        )

    except Exception as e:

        return f"Error : {e}"


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)