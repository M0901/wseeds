import streamlit as st  
import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt
import numpy as np


st.title("Wheat Seeds Dashbord")
df = pd.read_csv('seeds.csv')
st.dataframe(df)

st.write("*****************************************************************")

col1, col2 = st.columns(2)
with col1:
    
    st.dataframe(df[['Kernel.Length','Kernel.Width']])
with col2:
    st.header('Kernel Length & Kernel Width')
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:,3],df.iloc[:,4])
    st.pyplot(fig)   

st.write("*****************************************************************")
col1, col2 = st.columns(2)
with col1:
    
    st.dataframe(df[['Kernel.Length','Kernel.Groove']])
with col2:
    st.header('Kernel Length & Kernel Groove')
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:,3],df.iloc[:,6])
    st.pyplot(fig)     

st.write("*****************************************************************")
col1, col2 = st.columns(2)
with col1:
    
    st.dataframe(df[['Kernel.Width','Kernel.Groove']])
with col2:
    st.header('Kernel Width & Kernel Groove')
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:,4],df.iloc[:,6])
    st.pyplot(fig)    

st.write("*****************************************************************")
col1, col2 = st.columns(2)
with col1:
    
    st.dataframe(df[['Area','Perimeter']])
with col2:
    st.header('Area & Perimeter')
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:,0],df.iloc[:,1])
    st.pyplot(fig)     

st.write("***********************************************************************")
st.header('Line plot ')
st.line_chart(df[['Kernel.Length','Kernel.Width','Kernel.Groove']]) 

st.write("***********************************************************************")
st.header('Bar Chart')
st.bar_chart(df[['Kernel.Length','Kernel.Width','Kernel.Groove']]) 

st.write("***********************************************************************")
st.header('Line plot ')
st.line_chart(df[['Area','Perimeter','Asymmetry.Coeff']]) 

st.write("***********************************************************************")
st.header('Box Plot')
col1,col2,col3 =st.columns(3)
with col1:
    st.header('Kernel Length')
    fig, ax = plt.subplots()
    ax.boxplot(df.iloc[:,3])
    st.pyplot(fig)
with col2:
        st.header('Kernel Width')
        fig, ax = plt.subplots()
        ax.boxplot(df.iloc[:,4])
        st.pyplot(fig)
with col3:
    st.header('Kernel Groove')
    fig, ax = plt.subplots()
    ax.boxplot(df.iloc[:,6])
    st.pyplot(fig)