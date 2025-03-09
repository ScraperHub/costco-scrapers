from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

# Initialize Crawlbase API
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

# Fetch HTML content of product page
def fetch_product_page(url):
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

# Scrape product details from a Costco product page
def scrape_costco_product_page(url):
    html_content = fetch_product_page(url)

    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        title = soup.select_one('h1[automation-id="productName"]').text.strip() if soup.select_one('h1[automation-id="productName"]') else 'N/A'
        price = soup.select_one('span[automation-id="productPriceOutput"]').text.strip() if soup.select_one('span[automation-id="productPriceOutput"]') else 'N/A'
        rating = soup.select_one('div[itemprop="ratingValue"]').text.strip() if soup.select_one('div[itemprop="ratingValue"]') else 'N/A'
        description = soup.select_one('div[id="product-tab1-espotdetails"]').text.strip() if soup.select_one('div[id="product-tab1-espotdetails"]') else 'N/A'
        images_url = soup.find('img', class_='thumbnail-image')['src'] if soup.find('img', class_='thumbnail-image') else 'N/A'
        specifications = {row.select_one('.spec-name').text.strip(): row.select_one('div:not(.spec-name)').text.strip() for row in soup.select('div.product-info-description .row') if row.select_one('.spec-name')}

        product_details = {
            'title': title,
            'price': price,
            'rating': rating,
            'description': description,
            'images_url': images_url,
            'specifications': specifications,
        }

        return product_details
    else:
        return {}

# Save product details to a JSON file
def save_product_to_json(data, filename='costco_product_details.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

# Example usage
product_url = "https://www.costco.com/coddle-aria-fabric-sleeper-sofa-with-reversible-chaise-gray.product.4000223041.html"
product_details = scrape_costco_product_page(product_url)
save_product_to_json(product_details)