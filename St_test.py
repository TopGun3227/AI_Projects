#Activate virtual env for Python 
#C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects>.venv\Scripts\activate.bat
#(.venv) C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects>pip install streamlit
#(.venv) C:\Users\abhishek.ganguly\TopGun3227Repo\AI_Projects>streamlit run St_test.py
#You can now view your Streamlit app in your browser.
#Local URL: http://localhost:8501
#Network URL: http://192.168.1.3:8501
#Reference: https://github.com/pixegami/streamlit-demo-app

import streamlit as st
import pandas as pd
import numpy as np
#st.write("Hello, Streamlit!")
st.write("Welcome Abhishek!")
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
