import functools
import pandas as pd
from joblib import load
from sklearn.calibration import LabelEncoder

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/', methods=('GET', 'POST'))
def register():
    
    metric = request.args.get('metric')
    
    match metric:
        case 'Mass':
            MassPredict()
        case 'Coordenadas':
            CoordPredict()
        case 'Data':
            DatePredict()
    
    
    return render_template('index.html')


def MassPredict():
    recclass = request.args.get('recclass')
    year = request.args.get('year')
    reclat = request.args.get('reclat')
    reclong = request.args.get('reclong')
    
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
        
    else:
        print("Um ou mais valores não estão preenchidos")
        
def CoordPredict():
    recclass = request.args.get('recclass')
    year = request.args.get('year')
    reclat = request.args.get('reclat')
    reclong = request.args.get('reclong')
    
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
        
    else:
        print("Um ou mais valores não estão preenchidos")

