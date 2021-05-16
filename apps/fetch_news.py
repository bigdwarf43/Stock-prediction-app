import requests
import streamlit as st
import streamlit.components.v1 as components
api_key='ed0b00cc442c4ad183e455e7df4a477c'

def retrieve_news(company_name,company_ticker):
	main_url = "https://newsapi.org/v2/everything?q="+company_name+" OR "+company_ticker+" AND share OR stock&language=en&apiKey="+api_key
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

	news_images=[]
	for arti in fetched_articles:
		news_images.append(arti['urlToImage'])

	if not news_articles:
		st.header("no headlines")
	else:
		for i in range(len(news_articles)):
			my_expand = st.beta_expander(news_articles[i],False)
			#try:
			with my_expand:
				components.iframe(news_images[i],width=1200,height=500) #aletrnatives: st.image(news_images[i],use_column_width=True)	 #my_expand.markdown("![Alt Text]("+news_images[i]+")")
			#except:
				#print("no image")
			my_expand.write(news_desc[i])
			my_expand.write(news_links[i])
			st.markdown("&nbsp ")


def retrieve_business_news(category="business"):
	main_url = "https://newsapi.org/v2/top-headlines?q=stocks OR shares&category="+category+"&language=en&apiKey="+api_key
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

	news_images=[]
	for arti in fetched_articles:
		news_images.append(arti['urlToImage'])

	if not news_articles:
		st.header("no headlines")
	else:
		for i in range(len(news_articles)):
			st.markdown("## "+news_articles[i])
			st.markdown("&nbsp ")
			components.iframe(news_images[i],width=1200,height=500)
			st.write(news_desc[i])
			st.write(news_links[i])
			st.markdown("&nbsp ")

def retrieve_category_news(url):
	main_url = url
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

	news_images=[]
	for arti in fetched_articles:
		news_images.append(arti['urlToImage'])

	if not news_articles:
		st.header("no headlines")
	else:
		for i in range(len(news_articles)):
			st.markdown("## "+news_articles[i])
			st.markdown("&nbsp ")
			components.iframe(news_images[i],width=1200,height=500)
			st.write(news_desc[i])
			st.write(news_links[i])
			st.markdown("&nbsp ")




#st.markdown("![Alt Text]("+stock.info['logo_url']+")")