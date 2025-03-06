def fetch_url(url):
    import requests
    from requests.exceptions import RequestException

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html_content):
    from bs4 import BeautifulSoup

    return BeautifulSoup(html_content, 'html.parser')

def extract_data(soup, selector):
    return soup.select(selector)

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")