import streamlit as st
from .fetch_news import *

api_key='ed0b00cc442c4ad183e455e7df4a477c'

def app():
	st.info("# News module")
	selected_option = st.selectbox("Select category",('business','health','technolgy'))
	
	if selected_option == 'health':
		retrieve_category_news("https://newsapi.org/v2/everything?q=health&language=en&apiKey="+api_key)
	elif selected_option == 'technolgy':
		retrieve_category_news("https://newsapi.org/v2/everything?q=stocks OR shares AND technolgy&language=en&apiKey="+api_key)
	else:
		retrieve_category_news("https://newsapi.org/v2/everything?q=stocks OR shares&language=en&apiKey="+api_key)
