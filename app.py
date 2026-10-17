from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open("random_forest_health.pkl", "rb") as file:
    bundle = pickle.load(file)

model = bundle["model"]
encoders = bundle["encoders"]
feature_columns = bundle["feature_columns"]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API aksesibilitas layanan kesehatan berjalan"})


@app.route("/predict", methods=["POST"])
def predict():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"error": "Body harus berupa JSON"}), 400

    try:
        city = str(body["city"])
        taxonomy_name = str(body["taxonomy_name"])
        province = str(body["province"])
    except KeyError as e:
        return jsonify({"error": f"Field {e} wajib diisi"}), 400

    raw_input = {
        "CITY": city,
        "TAXONOMY_NAME": taxonomy_name,
        "PROVINCE": province,
    }

    encoded = {}
    for col, value in raw_input.items():
        encoder = encoders[col]
        if value not in encoder.classes_:
            return jsonify({
                "error": f"Kategori '{value}' tidak dikenal pada kolom {col}"
            }), 400
        encoded[col + "_enc"] = encoder.transform([value])[0]

    input_df = pd.DataFrame([encoded], columns=feature_columns)

    prediction = int(model.predict(input_df)[0])
    proba = model.predict_proba(input_df)[0]

    return jsonify({
        "prediction": "Y" if prediction == 1 else "N",
        "label": "Aksesibel" if prediction == 1 else "Tidak aksesibel",
        "probability": {
            "N": round(float(proba[0]), 4),
            "Y": round(float(proba[1]), 4),
        },
    })


if __name__ == "__main__":
    app.run(debug=True)