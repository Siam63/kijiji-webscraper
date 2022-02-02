import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

url = "https://www.kijiji.ca/b-oshawa-durham-region/fish/k0l1700275?rb=true&ll=43.865432%2C-79.048350&address=58+Brennan+Rd%2C+Ajax%2C+ON+L1T+1X4%2C+Canada&radius=12.0&dc=true"
page = requests.get(url)
webbrowser.open(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="mainPageContent")
ad_elements = results.find_all("div", class_="search-item")

for ad_element in ad_elements:
    title_element = ad_element.find("a", class_="title")
    print(title_element.text.strip())

# print(results.prettify())