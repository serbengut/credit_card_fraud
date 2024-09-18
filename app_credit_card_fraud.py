import pandas as pd

import streamlit as st
#from streamlit_echarts import st_echarts
from codigo_ejecucion_credit_card_fraud import *
import numpy as np
import cloudpickle
import pickle

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

st.set_page_config(
     page_title = 'Credit card fraud',
     #page_icon = 'DS4B_Logo_Blanco_Vertical_FB.png',
     layout = 'wide')

st.title('Credit Card fraud')

# vble. 1
distance_from_home = st.slider('Distancia desde casa en km', 0, 200)

# vble. 2
online_order = st.selectbox('Compra online', ['Sí', 'No'])
if online_order == 'Sí':
    online_order = 1
else:
    online_order = 0

# vble. 3
ratio_to_median_purchase_price = st.slider('Ratio entre valor de la compra y el valor de la mediana de las compras anteriores', 0, 10)

# vble. 4
repeat_retailer = st.selectbox('¿Has comprado alguna vez en esta tienda?', ['Sí', 'No'])
if repeat_retailer == 'Sí':
    repeat_retailer = 1
else:
    repeat_retailer = 0

registro = pd.DataFrame({'distance_from_home':distance_from_home,
                         'online_order':online_order,
                         'ratio_to_median_purchase_price':ratio_to_median_purchase_price,
                         'repeat_retailer':repeat_retailer}
                        ,index=[0])

registro

if st.sidebar.button('CALCULAR POSIBILIDAD DE FRAUDE'):

    precio = ejecutar_modelo(registro)

    precio

else:
    st.write('DEFINE LOS PARÁMETROS Y HAZ CLICK EN CALCULAR POSIBILIDAD DE FRAUDE')















