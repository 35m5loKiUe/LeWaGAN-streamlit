import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

import requests

'''
# TaxiFare Model
'''

st.markdown('''
#test api local
''')

url = 'http://127.0.0.1:8000/image'

#if url == 'https://taxifare.lewagon.ai/predict':

 #   st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

r = requests.get(url)

st.image(r)
