import pickle
import logging
from waitress import serve
from flask import Flask
from flask import request
from flask import jsonify
logging.basicConfig(level=logging.INFO)

output_file = 'model.bin'

# Load the model

with open(output_file, 'rb') as f_in: # replace w with r for reading
    dv, model = pickle.load(f_in)

app = Flask('House Price')

@app.route ('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X_data = dv.transform(data)
    y_pred = model.predict(X_data)

    result = {
        'price': int(y_pred)
    }
    return jsonify(result)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=9696)