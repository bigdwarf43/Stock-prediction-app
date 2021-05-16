import streamlit as st
from multiapp import MultiApp
from apps import home, stock, dashboard, news_module # importing app modules

app = MultiApp()
st.set_page_config(page_title="Prediticker", page_icon=None, layout='wide', initial_sidebar_state='collapsed')

app.add_app("Home", home.app)
app.add_app("Prediction", stock.app)
app.add_app("Dashboard", dashboard.app)
app.add_app("News", news_module.app)

app.run()

