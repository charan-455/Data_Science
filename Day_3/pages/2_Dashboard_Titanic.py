import streamlit as st
import os
from matplotlib import image
import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Dashboard - Titanic Data")

st.write("The Titanic dataset is a machine learning dataset that contains information on the passengers aboard the Titanic, including their survival status,gender, ticket class, age other details. The dataset is often used as a case study in data analysis and machine learning,The dataset has been widely used to develop and evaluate machine learning algorithms for predicting survival rates based on passenger details.")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "t.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)

st.header("Dataset:")
df = df.dropna()
df = df.drop(columns=['sibsp','parch','embarked','who','alone','adult_male','pclass','survived'])
st.dataframe(df)


option = ["Select","Survival Rate by Gender", "Survival Rate by Age", "Survival Rate by Class"]

st.header("Explore more:")
choice = st.selectbox("Choose a option",option)


if choice == "Survival Rate by Gender":
    st.header("Survival Rate by Gender")

    gender_survival = df.groupby(['sex', 'alive']).size().unstack()
    gender_survival.plot(kind='bar', stacked=True)
    st.pyplot()

elif choice == "Survival Rate by Age":
    st.header("Survival Rate by Age")

    df['Age_Group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 100], labels=['0-18', '18-35', '35-50', '50+'])
    age_survival = df.groupby(['Age_Group', 'alive']).size().unstack()
    age_survival.plot(kind='bar', stacked=True)
    st.pyplot()

elif choice == "Survival Rate by Class":
    st.header("Survival Rate by Class")
    st.markdown("::")
    class_survival = df.groupby(['class', 'alive']).size().unstack()
    class_survival.plot(kind='bar', stacked=True)
    st.pyplot()



