import scrapy


class BooksSpider(scrapy.Spider):
    name = "books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            book_url = book.css("h3 > a").attrib["href"]
            yield response.follow(book_url, callback=self.parse_book_page, meta={"test": "test string"})

        next_page = response.css("li.next > a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_book_page(self, response):
        book = response.css("div.product_main")[0]
        table_rows = response.css("table tr")
        yield {
            "url": response.url,
            "title": book.css("h1::text").get(),
            "price": book.css("p.price_color::text").get(),
            "rating": book.css("p.star-rating").attrib['class'],
            "category": response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            "upc": table_rows[0].css("td::text").get(),
            "product_type": table_rows[1].css("td::text").get(),
            "price_exl_tax": table_rows[2].css("td::text").get(),
            "price_incl_tax": table_rows[3].css("td::text").get(),
            "tax": table_rows[4].css("td::text").get(),
            "availability": table_rows[5].css("td::text").get(),
            "number_of_reviews": table_rows[6].css("td::text").get(),
            "description": response.css("#product_description ~ p::text").get(),
            "test": response.meta["test"]
        }
