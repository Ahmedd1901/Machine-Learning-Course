import streamlit as st
import pandas as pd
import numpy as np


st.title("Test App")
st.write("If you see this, Streamlit is working!")


## create a simple dataFrame 
df = pd.DataFrame(
    {
        'first column': [1,2,3,4],
        'second column':[10,20,30,40]
    }
)

## display the dataFrame
st.write("here is the DataFrame")
st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
