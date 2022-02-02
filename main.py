# Python code to make a web-scraper to make my life easier when posting and fetching ads on Kijiji

import requests
from bs4 import BeautifulSoup # library to parse structured data from a web browser; interact with HTML
from urllib.request import urlopen
import webbrowser

# URL = "https://realpython.github.io/fake-jobs/"
url = "http://olympus.realpython.org/profiles/aphrodite"
page = requests.get(url)
openPage = urlopen(url)

webbrowser.open(url)

#print(page.text) # fetches HTML code
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
# print(results.prettify())

# job_elements = results.find_all("div", class_="card-content")
# print(job_elements)

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
print()