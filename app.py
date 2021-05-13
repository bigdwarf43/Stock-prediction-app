import streamlit as st
from multiapp import MultiApp
from apps import home, stock # importing app modules

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Prediction", stock.app)

app.run()

