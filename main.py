import requests
from bs4 import BeautifulSoup

req = requests.get("https://en.wiktionary.org/wiki/Category:Cherokee_verbs")
soup = BeautifulSoup(req.content, "lxml")

tsal = soup.find_all("div", {"class": "mw-category-group"})[1].find_all("li")

data = ""
for _ in tsal:
    data += (_.find("a").get_text()) + "\n"

data = data.split("\n")
for _ in data:
    req = requests.get(f"https://en.wiktionary.org/wiki/{_}")
    soup = BeautifulSoup(req.content, "lxml")
    with open("out.csv", "a") as f:
        print(f"{_}," + soup.find("ol").get_text().replace("\n", "").replace(",", "\t"), file=f)
