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
            "href": response.request.url,
            "title": response.css("h1::text").get(),
            "category": response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            "price": response.css("p.price_color::text").get(),
            "upc": response.css("table.table-striped tr > td::text")[0].get(),
            "product_type": response.css("table.table-striped tr > td::text")[1].get(),
            "tax": response.css("table.table-striped tr > td::text")[4].get(),
            "availability": response.css("table.table-striped tr > td::text")[5].get(),
            "number_of_reviews": response.css("table.table-striped tr > td::text")[6].get(),
            "rating": response.css("p.star-rating").attrib['class'],
            "description": response.css("#product_description ~ p::text").get(),
            "test": response.meta["test"]
        }
