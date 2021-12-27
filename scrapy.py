import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.wikipedia.org/")

soup = BeautifulSoup(req.content, "html.parser")


print(soup.prettify());
# print(soup.get_text())
