# fetching news api and print user define type of news...

import requests
import json

query = input("What type of news are you interested in?: ")
url = f'https://newsapi.org/v2/everything?q={query}&from=2023-07-24&sortBy=publishedAt&apiKey=e5310e3398fc41188d1863389a769f9c'

r = requests.get(url)
news = json.loads(r.text)

for article in news['articles']:
    print(article['title'])
    print(article['description'])

    print('---------------------------------------------')