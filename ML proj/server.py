import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model
model = joblib.load("random_forest_model.pkl")

# Initialize Flask app
app = Flask(__name__)

# Define categorical mappings (same as training data)
categories = {
    "Favorite Color": ["Cool", "Neutral", "Warm"],
    "Favorite Music Genre": ["Rock", "Hip hop", "Folk/Traditional", "Jazz/Blues", "Pop"],
    "Favorite Beverage": ["Vodka", "Wine", "Whiskey", "Doesn't drink", "Beer", "Other"],
    "Favorite Soft Drink": ["7UP/Sprite", "Coca Cola/Pepsi", "Fanta"]
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Gender Prediction API is Running!"})

@app.route("/predict", methods=["POST"])
def predict_gender():
    try:
        # Get JSON request data
        data = request.get_json()

        # Convert input into DataFrame
        input_data = pd.DataFrame([data])

        # Encode categorical values
        for col in input_data.columns:
            if col in categories:
                input_data[col] = input_data[col].apply(lambda x: categories[col].index(x))

        # Make prediction
        prediction = model.predict(input_data)
        gender = "Female" if prediction[0] == 0 else "Male"

        return jsonify({"predicted_gender": gender})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
