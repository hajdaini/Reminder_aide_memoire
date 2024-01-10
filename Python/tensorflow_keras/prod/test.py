import requests
import json

url = "http://127.0.0.1:5000/api/flower"

payload = json.dumps({
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.5,
  "petal_width": 0.2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

if response.status_code != 200:
    print(f'Erreur : {response.status_code}')
    exit()

data = json.loads(response.text)
print(f'type: {data["class"]} with {float(data["percent"])*100}% confidence')
