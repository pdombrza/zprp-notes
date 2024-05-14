import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for q, a in zip(quotes, authors):
    print(f"{q.text} - {a.text}")
