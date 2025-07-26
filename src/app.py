from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/decision_tree_classifier_default_42.sav", "rb"))
class_dict = {
    "0": "Alumno no admitido",
    "1": "Alumno Admitido",
    
}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])
        val4 = float(request.form["val4"])
        val5 = float(request.form["val5"])
        val6 = float(request.form["val6"])
        
        data = [[val1, val2, val3, val4, val5, val6]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
