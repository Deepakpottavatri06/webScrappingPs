import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.bbc.com/news';


response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

anchors = soup.find_all('a', href=True)

with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])

    # Extract headlines text and URL
    for anchor in anchors:
        h2_tag = anchor.find('h2')
        if h2_tag:
            headline_text = h2_tag.text.strip()
            headline_url = anchor['href']
            if headline_url.startswith('/'):
                headline_url = 'https://www.bbc.com' + headline_url
            writer.writerow([headline_text, headline_url])

print("Data scraping complete and saved to headlines.csv")