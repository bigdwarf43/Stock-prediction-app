import streamlit as st
from multiapp import MultiApp
from apps import home, stock # importing app modules

app = MultiApp()

st.write("home page of stock app")


app.add_app("Home", home.app)
app.add_app("Prediction", stock.app)

app.run()

