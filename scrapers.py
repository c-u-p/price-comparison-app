import requests
from bs4 import BeautifulSoup

# Function to scrape Amazon
def scrape_amazon(product_name):
    url = f"https://www.amazon.com/s?k={product_name}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the price is within a span tag with class 'a-offscreen'
    price_tag = soup.find('span', class_='a-offscreen')
    if price_tag:
        price = price_tag.text.strip('$')
        return float(price.replace(',', ''))  # Remove commas in large prices
    return None  # If the price was not found

# Function to scrape eBay
def scrape_ebay(product_name):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the price is within a span tag with class 's-item__price'
    price_tag = soup.find('span', class_='s-item__price')
    if price_tag:
        price = price_tag.text.strip('$').replace(',', '')
        return float(price)
    return None
'''
# Function to scrape a fictional Website3
def scrape_website3(product_name):
    url = f"https://www.website3.com/search?q={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the price is within a div tag with class 'price'
    price_tag = soup.find('div', class_='price')
    if price_tag:
        price = price_tag.text.strip('$')
        return float(price)
    return None
'''