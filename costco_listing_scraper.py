from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

# Fetch HTML content
def fetch_search_listings(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000'
    }
    response = crawling_api.get(url, options)
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    else:
        print(f"Failed to fetch the page. Status code: {response['headers']['pc_status']}")
        return None

# Scrape product listings from a page
def scrape_costco_search_listings(url):
    html_content = fetch_search_listings(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        product_list = []
        product_items = soup.select('div[id="productList"] > div[data-testid="Grid"]')

        for item in product_items:
            title = item.select_one('div[data-testid^="Text_ProductTile_"]').text.strip() if item.select_one('div[data-testid^="Text_ProductTile_"]') else 'N/A'
            price = item.select_one('div[data-testid^="Text_Price_"]').text.strip() if item.select_one('div[data-testid^="Text_Price_"]') else 'N/A'
            rating = item.select_one('div[data-testid^="Rating_ProductTile_"] > div')['aria-label'] if item.select_one('div[data-testid^="Rating_ProductTile_"] > div') else 'N/A'
            product_url = item.select_one('a[data-testid="Link"]')['href'] if item.select_one('a[data-testid="Link"]') else 'N/A'
            image_url = item.find('img')['src'] if item.find('img') else 'N/A'

            product_list.append({
                'title': title,
                'price': price,
                'rating': rating,
                'product_url': product_url,
                'image_url': image_url
            })
        return product_list
    else:
        return []

# Scrape all pages
def scrape_all_pages(base_url, total_pages):
    all_products = []
    for page_num in range(1, total_pages + 1):
        paginated_url = f"{base_url}&currentPage={page_num}"
        print(f"Scraping page {page_num}")
        products = scrape_costco_search_listings(paginated_url)
        all_products.extend(products)
    return all_products

# Save data to a JSON file
def save_to_json(data, filename='costco_product_listings.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

# Example usage
base_url = "https://www.costco.com/s?dept=All&keyword=sofas"
total_pages = 5
all_products = scrape_all_pages(base_url, total_pages)
save_to_json(all_products)