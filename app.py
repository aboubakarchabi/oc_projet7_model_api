# -*- coding: utf-8 -*-
from joblib import load
from flask import Flask, jsonify, request

app = Flask(__name__)

# load model
model = load('pipeline1_credit1.joblib')

@app.route("/predict", methods = ["POST"])
def predict():

    data = request.get_json(force=True)


    prediction = model.predict([list(data.values())])

    output = prediction[0]
    return jsonify({"prediction": int(output)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
