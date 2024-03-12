
# 01_streamlit

import streamlit as st

st.title('Gruppo Nucleare')

st.write('Ciao a tutti !!!!')



x = 4
st.write('x cube is ', x * x * x)

y = st.slider('slider per y')
st.write('selected value', y)

z = st.sidebar.slider('altro slider')

st.write('x + y + z', x + y + z)

city = st.selectbox(
    'scegli una città',
    ['Roma', 'Sicilia', 'Napoli']
)

st.write('Hai selezionato', city)

import numpy as np
import pandas as pd
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


st.write('CIAO')




# PROGRESS BAR
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'




























