import functools
import pandas as pd
from joblib import load
from sklearn.calibration import LabelEncoder

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route('/', methods = ['GET', 'POST'])
def index(): 
    # return render_template('index.html')

# @bp.route('/', methods=[])
# def register():
    
    answer = ""
    if request.method == "POST":
        metric = request.form.get('metric')
        match metric:
            case "massa":
                answer = MassPredict()
            case "latitude":
                answer = LatPredict()
            case "longitude":
                answer = LongPredict()    
    return render_template('index.html', answer=answer)


def MassPredict():
    recclass = request.form.get('recclass')
    year = request.form.get('year')
    reclat = request.form.get('reclat')
    reclong = request.form.get('reclong')
    
    le = load(open("label_encoder.pkl", 'rb'))
    
    if all(value is not None for value in [recclass, year, reclat, reclong]):
        infoArray = {
            "recclass": [recclass],
            "year": [year],
            "reclat": [reclat],
            "reclong": [reclong]
        }
    
        df = pd.DataFrame(infoArray)
        
        df['recclass'] = le.transform(df['recclass'])
        
        loaded_model = load(open("randomForestMass.pkl", 'rb'))
        
        predict = loaded_model.predict(df)
        
        answer = str(predict[0])
        print(answer)
        
        return answer
        
    else:
        print("Um ou mais valores não estão preenchidos")
        
def LatPredict():
    recclass = request.form.get('recclass')
    mass = request.form.get('massa')
    year = request.form.get('year')
    long = request.form.get('long')
    
    le = load(open("label_encoder.pkl", 'rb'))
    
    if all(value is not None for value in [recclass, year]):
        infoArray = {
            "recclass": [recclass],
            "mass": [mass],
            "year": [year],
            "reclong": [long]
        }
    
        df = pd.DataFrame(infoArray)
        
        df['recclass'] = le.transform(df['recclass'])
        
        loaded_model = load(open("decisionTreeLat.pkl", 'rb'))
        
        predict = loaded_model.predict(df)
        
        answer = str(predict[0])
        
        print("lat: ", answer)
        
        return answer
        
    else:
        print("Um ou mais valores não estão preenchidos")


def LongPredict():
    recclass = request.form.get('recclass')
    mass = request.form.get('massa')
    year = request.form.get('year')
    lat = request.form.get('lat')
    
    le = load(open("label_encoder.pkl", 'rb'))
    
    if all(value is not None for value in [recclass, year]):
        infoArray = {
            "recclass": [recclass],
            "mass": [mass],
            "year": [year],
            "reclat": [lat]
        }
    
        df = pd.DataFrame(infoArray)
        
        df['recclass'] = le.transform(df['recclass'])
        
        loaded_model = load(open("decisionTreeLong.pkl", 'rb'))
        
        predict = loaded_model.predict(df)
        
        answer = str(predict[0])
        
        print("long: ", answer)
        return answer
        
    else:
        print("Um ou mais valores não estão preenchidos")

