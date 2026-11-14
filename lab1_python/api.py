import os
import requests
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("NEWS_API_KEY")


class Article:
    def __init__(self, title, source, url):
        self.title = title
        self.source = source
        self.url = url

    def show(self):
        print("Title :", self.title)
        print("Source:", self.source)
        print("Link  :", self.url)
        print("-" * 40)


url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}"
data = requests.get(url).json()

for item in data["articles"]:
    Article(item["title"], item["source"]["name"], item["url"]).show()