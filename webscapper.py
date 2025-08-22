import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.string
print("Page Title:", title)

with open("web_title.txt", "w") as f:
    f.write("Page Title: " + title)
