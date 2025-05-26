# Books to scrape
Scraping [https://books.toscrape.com/](https://books.toscrape.com/)

------------------------------------------------------
## Description
Scrape all book listings from the site, extracting details such as title, price, stock availability, rating, and going to get deeper data from individual book pages (e.g.: UPC, product description)

- URL: https://books.toscrape.com/
- Structure: Pagination-based e-commerce website.
- Content: 1000 books across 50 pages.
------------------------------------------------------
## Installation
1. Clone the repository:
    ```sh 
    git clone https://github.com/Lando-Scraping/ClaudeAI_LocationExtractor.git
   ```
2. Install the required dependencies:
    ```sh 
    pip install -r requirements.txt
   ```
------------------------------------------------------
## How to run
1. Go to the project directory:
   ```sh 
   cd ~/Projects/Scrapy/books
   ```
2. Run this to get json file:
   ```sh 
   scrapy crawl books_spider -o books.json  
   ```
