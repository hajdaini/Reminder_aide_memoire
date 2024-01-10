from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/flower', methods=['POST'])
def flower():
    url = "http://127.0.0.1:5000/api/flower"
    data = {
        "sepal_length": request.form.get('sepal_length'),
        "sepal_width": request.form.get('sepal_width'),
        "petal_length": request.form.get('petal_length'),
        "petal_width": request.form.get('petal_width')
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()
    data = response.json()
    return "Type: {} with {}% confidence".format(data["class"], float(data["percent"]) * 100)

if __name__ == '__main__':
    app.run(debug=True, port=8000)