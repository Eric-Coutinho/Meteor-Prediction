import functools
import pandas as pd

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/', methods=('GET', 'POST'))
def register():
    recclass = request.args.get('recclass')
    year = request.args.get('year')
    reclat = request.args.get('reclat')
    reclong = request.args.get('reclong')
    
    if all(value is not None for value in [recclass, year, reclat, reclong]):
        infoArray = {
            "recclass": [recclass],
            "year": [year],
            "reclat": [reclat],
            "reclong": [reclong]
        }
    
        df = pd.DataFrame(infoArray)
    
        print(df)
        
    else:
        print("Um ou mais valores não estão preenchidos")  
    
    return render_template('index.html')



