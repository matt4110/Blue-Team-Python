import requests
from bs4 import BeautifulSoup

URL = "https://letsdefend.io"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("meta", {"name":"description"})

print(results)