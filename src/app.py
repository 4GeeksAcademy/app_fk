from flask import Flask, request, render_template
import os
from joblib import load

app = Flask(__name__)
try:
    model_path = os.path.join('..', 'models', 'random_forest_regressor_default_42.sav')
    
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            model = load(file)
        print("✅ Modelo cargado correctamente!")
        print(f"Tipo de modelo: {type(model)}")
        
        # Ejemplo de uso:
        # predictions = model.predict(X_new_data)
    else:
        raise FileNotFoundError(f"No se encontró el archivo en {model_path}")
        
except Exception as e:
    print(f"❌ Error al cargar el modelo: {str(e)}")


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        val4 = float(request.form["val4"])
        
        
        data = [[val1, val2, val3, val4]]
        prediction = str(model.predict(data)[0])
        #pred_class = class_dict[prediction]
    else:
        prediction = None
    
