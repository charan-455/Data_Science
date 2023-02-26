import streamlit as st
import os
import altair as alt
from matplotlib import image
import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Dashboard - Titanic Data")

st.write("The tips dataset is a commonly used dataset in data analysis and machine learning, containing information on customers who visited a restaurant and the amount they tipped. The dataset includes features such as the total bill, tip amount, day of the week, time of day, and other customer information. The tips dataset is often used to explore relationship between tips and other factors such as the day of the week or time of day. The dataset has also been used to develop and evaluate machine learning models for predicting tip amounts based on customers.")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "tips.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "tips.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
df = df.drop(columns=['sex'])

df = df.dropna()
st.header("Dataset:")
st.dataframe(df)

filtered_data = df[(df['tip'] >=0.50) & (df['tip'] <= 10)]

option = ["Select","Day", "Time","Size","Total_Bill"]

st.header("Explore more:")
choice = st.selectbox("Choose a option",option)



if choice == "Total_Bill":
    st.header("Total_Bill vs Tip")
    sns.scatterplot(data=df, x='total_bill', y='tip')
    st.pyplot()

elif choice == "Day":
    st.header("Day vs Tip")
    grouped_data = filtered_data.groupby('day').mean().reset_index()
    bar_chart = alt.Chart(grouped_data).mark_bar().encode(x='day', y='tip')
    st.altair_chart(bar_chart, use_container_width=True)

elif choice == "Time":
    st.header("Time vs Tip")
    grouped_data = filtered_data.groupby('time').mean().reset_index()
    bar_chart = alt.Chart(grouped_data).mark_bar().encode(x='time', y='tip')
    st.altair_chart(bar_chart, use_container_width=True)
    
elif choice == "Size":
    st.header("Size vs Tip")
    grouped_data = filtered_data.groupby('size').mean().reset_index()
    bar_chart = alt.Chart(grouped_data).mark_bar().encode(x='size', y='tip')
    st.altair_chart(bar_chart, use_container_width=True)











