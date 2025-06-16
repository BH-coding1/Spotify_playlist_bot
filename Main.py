import requests
from bs4 import BeautifulSoup
from scraping import Scraper
def main():
    bot = Scraper()
    bot.scrape()


if __name__ =='__main__':
    main()