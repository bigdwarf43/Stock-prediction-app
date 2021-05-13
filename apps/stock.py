import streamlit as st
from datetime import date
import requests

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news



def app():
	

	invalidTicker = False
	START = "2015-01-01"
	TODAY = date.today().strftime("%Y-%m-%d")

	st.title("Stock price prediction")

	selected_stock = st.text_input("Enter ticker", "GOOG")

	n_years = st.slider("Years of prediction:", 1, 4)
	period = n_years * 365

	@st.cache
	def load_data(ticker):
		data = yf.download(ticker, START, TODAY)
		data.reset_index(inplace = True)
		if data.empty:
			st.write("invalid ticker")
			invalidTicker = True
		else:
			return data

	if invalidTicker == True:
		st.write("enter a valid ticker")

	else:
		
		data_load_state = st.info("Load data...")
		data = load_data(selected_stock)
		data_load_state.success("Loading data...done!")

		st.info('Raw data')
	
		st.write(data.tail())


		def plot_raw_data():
			fig = go.Figure()
			fig.add_trace(go.Scatter(x =data['Date'], y=data['Open'], name='stock_open'))
			fig.add_trace(go.Scatter(x =data['Date'], y=data['Close'], name='stock_close'))
			fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible = True)
			st.plotly_chart(fig)

		plot_raw_data()


		#Forecasting
		df_train = data[['Date', 'Close']]
		df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

		m = Prophet()
		m.fit(df_train)
		future = m.make_future_dataframe(periods=period)
		forecast = m.predict(future)

		st.info('Raw forecast data')
		st.write(forecast.tail())

		st.info('Forecast data')

		fig1 = plot_plotly(m, forecast)
		st.plotly_chart(fig1)

		st.info('Forecast components')
		fig2 = m.plot_components(forecast)
		st.write(fig2)	

		st.info("Top headlines regarding the "+selected_stock+" stock")
		retrieve_news(selected_stock)


