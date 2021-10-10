from scrapygoodnews.scrapygoodnews.spiders.goodnews_scrape import Goodnews
import scrapygoodnews.scrapygoodnews.settings as my_settings
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess



def run_spider():
    """run spider with Goodnews"""
    # Import settings from project and not terminal default path
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)

    crawler = CrawlerProcess(crawler_settings)
    # Avoid Twisted reactor issue - For running the same notebook
    print("Spider start running\n /╲/\\(╭ •̀ •́╮)/\\╱\\ \t /╲/\\(╭ •̀ •́╮)/\╱\\ \t /╲/\\(╭ •̀ •́╮)/\\╱\\")
    crawler.crawl(Goodnews)
    crawler.start(stop_after_crawl=False)
    # print("Spider end")

    #crawler.start(stop_after_crawl=False)