from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
with open('../models/random_forest_regressor_default_42.sav', 'rb') as file:
    model = pickle.load(file)


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
    
