from flask import Flask, request, jsonify
from model import predict_flower

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Flower Predictor</h1>'

@app.route('/api/flower', methods=['POST'])
def flower_prediction():
    sample_json = request.json
    result = predict_flower(sample_json)
    print(result)
    return jsonify(result)  # Utilisez jsonify pour assurer une sérialisation JSON correcte


if __name__ == '__main__':
    app.run(debug=True)
