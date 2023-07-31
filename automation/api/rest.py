import requests

def get_news(topic,from_date,to_date,language="en",apiKey="890603a55bfa47048e4490069ebee18c"):
    return f"https://newsapi.org/v2/{topic}?qInTitle=stock%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={apiKey}"

data = requests.get(get_news(topic="everything",from_date="2023-7-27",to_date="2023-7-28"))
content = data.json()
print(type(content))
#print(content["articles"])
articles = content["articles"]
print(content["articles"][0]["title"])
print(content["articles"][0]["description"])

results = []
for article in articles:
    results.append("TITLE:\n {article['title']} \nDESCRIPTION:\n {article['description']}")