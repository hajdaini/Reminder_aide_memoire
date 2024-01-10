import numpy as np
from tensorflow.keras.models import load_model
import joblib


model = load_model("iris_model.keras")
scaler = joblib.load("iris_scaler.pkl")

def predict_flower(sample_json):
    """
    Cette fonction prend en entrée un modèle, un scaler et un dictionnaire contenant les caractéristiques d'une fleur à prédire.
    Elle retourne la prédiction du modèle pour la fleur donnée.

    Paramètres :
    - model : Le modèle utilisé pour effectuer la prédiction.
    - scaler : Le scaler utilisé pour normaliser les données.
    - sample_json : Un dictionnaire contenant les caractéristiques de la fleur à prédire.

    Retour :
    - La prédiction du modèle pour la fleur donnée.
    """
    
    s_len = sample_json["sepal_length"]
    s_width = sample_json["sepal_width"]
    p_len = sample_json["petal_length"]
    p_width = sample_json["petal_width"]

    flower = [[s_len, s_width, p_len, p_width]]
    flower = scaler.transform(flower)

    classes = np.array(["setosa", "versicolor", "virginica"])
    prediction = model.predict(flower)[0]
    class_ind = int(np.argmax(prediction))
    percent = round(prediction[class_ind], 2)
    return {"class": classes[class_ind], "percent": str(percent)}