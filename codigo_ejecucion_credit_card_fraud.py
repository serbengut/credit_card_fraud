import numpy as np
import pandas as pd
import cloudpickle

#Automcompletar rápido
#%config IPCompleter.greedy=True

from janitor import clean_names

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import MinMaxScaler

from sklearn.ensemble import HistGradientBoostingClassifier

from xgboost import XGBClassifier

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline


def ejecutar_modelo(df):
   
    nombre_pipe_ejecucion = 'pipe_ejecucion.pickle'

    with open(nombre_pipe_ejecucion, mode='rb') as file:
        pipe_ejecucion = cloudpickle.load(file)

    scoring = pipe_ejecucion.predict_proba(df)[:,1]

    return 'El porcentaje de ser fraude es: {}%'.format(round(scoring[0]*100,2))



