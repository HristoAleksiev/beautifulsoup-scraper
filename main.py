from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

news_titles = soup.select(selector="table tr td .storylink")
news_upvotes = soup.select(selector="table tr .subtext .score")
news_titles = [{
    "title": title.text,
    "link": title.get("href"),
    "score": int(score.text.split(" ")[0])
    }
    for title, score in zip(news_titles, news_upvotes)]

news_max_upvotes = max(news_titles, key=lambda score: score["score"])
print(news_max_upvotes)
