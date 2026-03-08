import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"hello, {name}")
age = st.slider("select your age:",0,100,25)
st.write(f'your age is {age}')

options = ['Python','Java','C++','Javascript']
choice = st.selectbox("choose your favourite language", options)
st.write(f'you chose {choice}')

data = {
    'name' : ['ahmed','mohamed','mahmoud','ali'],
    'age'  : [25,21,23,24],
    'city' : ['cairo','alexandria','hurghada','sharm elsheikh']
 }

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file = st.file_uploader("choose a csv file",type = 'csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)