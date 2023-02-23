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

url = 'http://127.0.0.1:8000/image?v1=1&v2=1&v3=2&v4=1&v5=2&v6=1&v7=2&v8=1&v9=2&v10=1'


r = requests.get(url)

st.image(r)
