import streamlit as st

title = '<h1 style="color: red;">Innomatics Data App</h1>'
st.markdown(title, unsafe_allow_html=True)

st.snow()
st.balloons()

st.header("Welcome to the Data Science World.....")

st.write("In this section app we are going to learn about three data sets and some plots:")

st.markdown("""
* __IRIS dataset__
* __Titanic dataset__
* __Tips dataset__
""")

st.write("Click on left side arrow to know about the datasets")

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("Lets begin our journey:blush:")
    st.snow()
    st.balloons()
