import requests
from bs4 import BeautifulSoup
url = "http://www.bizjournals.com/stlouis/news/2013/12/30/year-in-review-the-10-biggest-funding.html"

page = requests.get(url)

data = page.text

soup = BeautifulSoup(data)

print soup
