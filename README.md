# costco-scrapers

## Description

This repository contains Python-based scrapers for extracting product listings and detailed product information from Costco. These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data is processed using BeautifulSoup for HTML parsing and Pandas for structured storage.

➡ Read the full blog [here](https://crawlbase.com/blog/scrape-costco-product-data/) to learn more.

## Scrapers Overview

### Costco Product Listing Scraper

The Costco Product Listing Scraper (`costco_listing_scraper.py`) extracts:

- **Product Title**
- **Price**
- **Product URL**
- **Rating**
- **Thumbnail Image**

The scraper supports pagination, ensuring comprehensive data extraction. The extracted data is saved in a JSON file.

## Costco Product Detail Scraper

The Costco Product Detail Scraper (`costco_product_scraper.py`) extracts detailed product information, including:

- **Product Title**
- **Full Description**
- **Price**
- **Specifications**
- **Rating**
- **Image URL**

The extracted data is saved in a JSON file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if required (for Linux/macOS)
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

### Get Your Crawlbase Access Token

1. Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
2. Use the JS token for Costco scraping, as the site uses JavaScript-rendered content.

## Update the Scraper with Your Token

Replace "`YOUR_CRAWLBASE_API_KEY`" in the script with your Crawlbase JS Token.

Run the Scraper

```bash
# For product listing scraping
python costco_listing_scraper.py

# For product detail scraping
python costco_product_scraper.py
```

The scraped data will be saved in `costco_product_listings.json` or `costco_product_details.json`, depending on the script used.

## To-Do List

- Expand scrapers to extract additional product details like discounted prices and available coupons.
- Optimize data storage and add support for CSV and database integration.
- Implement asynchronous requests to speed up data extraction.
- Enhance scraper efficiency with Crawlbase Smart Proxy to prevent blocks.
- Automate scheduled scraping for real-time price monitoring and product tracking.

## Why Use This Scraper?

- ✔ **Bypasses anti-bot protections** with Crawlbase.
- ✔ **Handles JavaScript-rendered content** seamlessly.
- ✔ **Extracts accurate and structured product data** efficiently.
