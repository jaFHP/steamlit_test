import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('Hellooo Bastar Craton')
st.write('**This is just a test for the Data Science Short Course @goetheUniFrankfurt**')

#import Georoc File
df=pd.read_csv('data/Bastar Craton.csv')

cat_names=df.columns.tolist()[27:]

st.multiselect('select please',[1,2,3])
col1, col2 = st.columns([.3, .7])
with col1:
    el1 = st.selectbox('Please select an element for x-axis', cat_names)
    el2 = st.selectbox('Please select an element for y-axis', cat_names)
with col2:
    fig=plt.figure()
    plt.scatter(df[el1],df[el2])
    plt.xlabel(f'hello {el1}')
    plt.ylabel(f'hello {el2}')
    st.pyplot(fig)

tab1, tab2 = st.tabs(['x-axis', 'DOG'])

with tab1:
    st.header('about')
    st.write('this app shows plots')
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
st.dataframe(df)