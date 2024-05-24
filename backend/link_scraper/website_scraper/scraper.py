import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for HTTP errors
    soup = BeautifulSoup(response.text, 'html5lib')
    title = soup.title.string if soup.title else url

    links = []

    for a_tag in soup.find_all('a', href=True):
        link_url = a_tag['href']
        link_text = ''.join(a_tag.stripped_strings) # Get text content 
        links.append({
            'url': link_url,
            'name': link_text,
        })
    
    return title, links
