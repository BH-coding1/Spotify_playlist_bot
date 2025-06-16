import requests
from bs4 import BeautifulSoup
import datetime

class Scraper:
    def __init__(self):
        self.date = str(input('ENTER THE DATE YOU ARE LOOKING FOR (YYYY-MM-DD): '))
        self.url = f'https://www.billboard.com/charts/hot-100/{self.date}'
    def scrape(self):
        # getting the response
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'}
        self.response = requests.get(url=self.url,headers=self.header)
        print('Success' if self.response.raise_for_status() == None else self.response.raise_for_status() )
        self.html_data = self.response.text
        # scraping the html_data
        self.soup = BeautifulSoup(self.html_data,'html.parser')

        #getting the song name elements
        self.song_name_elements = self.soup.select('ul li ul li h3')

        #getting only the text from the elements
        self.song_name_texts = [song_element.text.strip() for song_element in self.song_name_elements ]

        print(self.song_name_texts)










