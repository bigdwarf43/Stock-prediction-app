import requests
import streamlit as st
api_key='ed0b00cc442c4ad183e455e7df4a477c'

def retrieve_news(company_ticker):
	main_url = "https://newsapi.org/v2/everything?q="+company_ticker+"&language=en&apiKey="+api_key
	news = requests.get(main_url).json()

	fetched_articles = news['articles']

	news_articles=[]
	for arti in fetched_articles:
		news_articles.append(arti['title'])

	news_links=[]
	for arti in fetched_articles:
		news_links.append(arti['url'])

	news_desc=[]
	for arti in fetched_articles:
		news_desc.append(arti['description'])

	if not news_articles:
		st.header("no headlines")
	else:
		for i in range(len(news_articles)):
			my_expand = st.beta_expander(news_articles[i],False)
			my_expand.write(news_desc[i])
			my_expand.write(news_links[i])
