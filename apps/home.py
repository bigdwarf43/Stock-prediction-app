import streamlit as st


def app():
	st.title("home page")

	st.write("this is a 'home page'")

	news = st.beta_container()

	with news:
		st.header('hello')