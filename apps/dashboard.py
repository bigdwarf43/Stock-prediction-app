import streamlit as st
from datetime import date
import requests
from yahoo_fin import stock_info as si


import yfinance as yf
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news

def app():

    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    st.title("Stock Overview")

    selected_stock = st.text_input("Enter ticker","GOOG")
    st.markdown("&nbsp ")

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace = True)
        return data

    data = load_data(selected_stock)

    stock = yf.Ticker(selected_stock)

    col1, col2, col3= st.beta_columns([2,1,1])
    


    #st.write(stock.info) #output all stock info in json
    with col1:
        st.markdown("# "+stock.info['longName'])
        st.markdown("**"+stock.info['exchange']+"** ***"+stock.info['exchangeTimezoneName']+"***")
        st.image(stock.info['logo_url'],use_column_width='auto')#st.markdown("![Alt Text]("+stock.info['logo_url']+")")
        
       

    with col2:
        st.markdown("&nbsp ")
        st.success("**Current price:** "+str(si.get_live_price(selected_stock))+" "+stock.info['currency'])
        st.info("**Today open:** "+str(stock.info['open'])+" "+stock.info['currency'])
        st.warning("**Previous Close:** "+str(stock.info['previousClose'])+" "+stock.info['currency'])
        
    with col3:
        st.empty()
        

    st.markdown("&nbsp ")

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x =data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x =data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text ="Time series data", xaxis_rangeslider_visible = True, font=dict(family="Sans serif",size=18),margin=dict(l=10, r=10, t=40, b=30))
        st.plotly_chart(fig)

 
    plot_raw_data()

    st.markdown("&nbsp ")

    stock_info, company_info = st.beta_columns(2)

    with stock_info:
        st.info("**Stock Information**")
    with company_info:
        st.info("**Company info**")

    company_info_col1,company_info_col2, company_info_col3 = st.beta_columns([1,1,2])

   
    with company_info_col1:
        st.markdown("**quote type:** "+stock.info['quoteType'])
        st.markdown("**52 week high:** "+str(stock.info['fiftyTwoWeekHigh']))
        st.markdown("**52 week low:** "+str(stock.info['fiftyTwoWeekLow']))
        st.markdown("**Regular Day high:** "+str(stock.info['regularMarketDayHigh']))
        st.markdown("**Regular Day low:** "+str(stock.info['regularMarketDayLow']))
        
        st.markdown("**Volume:** "+str(stock.info['volume']))
        st.markdown("**Sector:** "+stock.info['sector'])
    with company_info_col2:
        st.markdown("**Peg ratio:** "+str(stock.info['pegRatio']))
        st.markdown("**Price to book:** "+str(stock.info['priceToBook']))
        st.markdown("**Book value:** "+str(stock.info['bookValue']))
        st.markdown("**forward eps:** "+str(stock.info['forwardEps']))
        st.markdown("**Trailing eps:** "+str(stock.info['trailingEps']))
        st.markdown("**Earnings quarterly growth:** "+str(stock.info['earningsQuarterlyGrowth']))
        st.markdown("**Revenuew quarterly growth:** "+str(stock.info['revenueQuarterlyGrowth']))
    with company_info_col3:
        st.markdown("**Website:** "+stock.info['website'])
        st.markdown("**Industry:** "+stock.info['industry'])
        st.markdown("**Market Cap:** "+str(stock.info['marketCap']))

    st.markdown("&nbsp ")
    st.info("**Business summary**")
    st.write(stock.info['longBusinessSummary'])

    st.markdown("&nbsp ")

    st.info("**Top headlines regarding the** "+selected_stock+" **stock**")
    retrieve_news(stock.info['shortName'],stock.info['symbol'])



#day high low
#52 week high low

#company essential
#market cap,no of share, pe ratio, pb ratio, face value, forward and trailing eps, growth earning and revenue
