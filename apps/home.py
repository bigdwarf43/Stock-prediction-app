import streamlit as st
from .fetch_news import retrieve_business_news
import requests
import pandas as pd
from datetime import date
import yfinance as yf
from yahoo_fin import stock_info as si
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

def app():


	st.markdown("# Prediticker")
	st.write("&nbsp")

	stock = yf.Ticker("^IXIC")
	#st.write(stock.info)
	def load_data(component):
		component_data=si.get_quote_data(component)
		return component_data

	NASDAQ_data = load_data("^IXIC")
	NIFTY50_data = load_data("^NSEI")
	BSESENSEX_data = load_data("^BSESN")
	#st.write(NASDAQ_data)

	def write_data(component):
		if component['regularMarketChange'] > 0:
			st.success("**"+str(component['shortName'])+"** "+component['marketState']+
				"\n\n __"+str(component['regularMarketPrice'])+
				"__ +"+str(component['regularMarketChange'])+
				" (+"+str(component['regularMarketChangePercent'])+")")
				
		else:
			st.error("**"+str(component['shortName'])+"** "+component['marketState']+
				"\n\n __"+str(component['regularMarketPrice'])+
				"__ "+str(component['regularMarketChange'])+
				" ("+str(component['regularMarketChangePercent'])+")")

	col1, col2, col3 = st.beta_columns(3)

	with col1:
		write_data(NASDAQ_data)
	with col2:
		write_data(NIFTY50_data)
	with col3:
		write_data(BSESENSEX_data)

	st.write("&nbsp")
	gainer_col, loser_col, active_col = st.beta_columns([1,1,1])


	gainers=si.get_day_gainers().head(10)
	gainers.drop(gainers.columns[[6,8]], axis=1, inplace=True)
	with gainer_col:
		st.success("**Top gainers**")
		st.dataframe(gainers)

	losers=si.get_day_losers().head(10)
	with loser_col:
		st.error("**Top losers**")
		st.dataframe(losers)

	active=si.get_day_most_active().head(10)
	with active_col:
		st.warning("**Top active**")
		st.dataframe(active)

	st.markdown("&nbsp ")

	st.info("# Today's top headlines")
	

	retrieve_business_news()