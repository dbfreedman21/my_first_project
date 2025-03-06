import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html_content):
    return BeautifulSoup(html_content, 'html.parser')

def extract_data(soup, selector):
    elements = soup.select(selector)
    return [element.get_text(strip=True) for element in elements]

def scrape(url, selector):
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        return extract_data(soup, selector)
    return []