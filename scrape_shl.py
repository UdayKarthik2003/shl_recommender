import requests
from bs4 import BeautifulSoup
import json
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

html_content = response.text
soup = BeautifulSoup(html_content, "lxml")  # ✅ This line goes here
print(soup.title.text)  # or anything else you want to extract

BASE_URL = "https://www.shl.com"
CATALOG_URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape_assessments():
    response = requests.get(CATALOG_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("a", class_="catalog-tile-link")

    assessments = []
    for card in cards:
        title = card.find("div", class_="catalog-tile-title").text.strip()
        url = BASE_URL + card["href"]
        details = {
            "name": title,
            "url": url,
            "duration": "N/A",
            "remote": "Yes",     # Update if scrapeable
            "adaptive": "Yes",   # Update if scrapeable
            "type": "N/A"
        }
        assessments.append(details)

    with open("assessments.json", "w") as f:
        json.dump(assessments, f, indent=2)

if __name__ == "__main__":
    scrape_assessments()
