import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

import requests

'''
# WaGAN image
'''

st.markdown('''
#test api local
''')

url = 'http://127.0.0.1:8000/image'


r = requests.get(url)

st.image(r)
