import streamlit as st
import os
from dotenv import load_dotenv

import requests

'''
# WaGAN image
'''

load_dotenv()


st.markdown('''
#test api local
''')

col1, col2 = st.columns(2)

with col1:

    v1 = st.slider('layer1', min_value=1, max_value=10)
    v2 = st.slider('layer2', min_value=1, max_value=10)
    v3 = st.slider('layer3', min_value=1, max_value=10)
    v4 = st.slider('layer4', min_value=1, max_value=10)
    v5 = st.slider('layer5', min_value=1, max_value=10)
    v6 = st.slider('layer6', min_value=1, max_value=10)
    v7 = st.slider('layer7', min_value=1, max_value=10)
    v8 = st.slider('layer8', min_value=1, max_value=10)
    v9 = st.slider('layer9', min_value=1, max_value=10)
    v10 = st.slider('layer10', min_value=1, max_value=10)

params_api = {'v1':v1,
          'v2':v2,
          'v3':v3,
          'v4':v4,
          'v5':v5,
          'v6':v6,
          'v7':v7,
          'v8':v8,
          'v9':v9,
          'v10':v10}

url = 'https://lewagandocker-vl3hfwrb3a-ew.a.run.app/image?'


res = requests.get(url, params=params_api)

with col2:

    if res.status_code == 200:
            ### Display the image returned by the API
            st.image(res.content, caption="Image returned from API ☝️")
    else:
            st.markdown("**Oops**, something went wrong 😓 Please try again.")
            print(res.status_code, res.content)


#st.image(r)
