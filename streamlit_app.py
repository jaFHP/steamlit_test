import streamlit as st
import pandas as pd
st.title('Hellooo Bastar Craton')
st.write('**This is just a test for the Data Science Short Course @goetheUniFrankfurt**')

#import Georoc File
df=pd.read_csv('data/Bastar Craton.csv')
st.dataframe(df)
