from requests import Session
from bs4 import BeautifulSoup
import AddressParser
import os


class Scraper:

    def __init__(self):
        self.session = Session()
        self.session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        self.parser = BeautifulSoup
        self.main_source_of_zip = "https://worldpostalcode.com/"
        self.walmart_finder = "https://www.walmart.com/store/finder?location=[location / zipcode]&distance=100"

    def parse_zipCode(self):

        if not os.path.exists("parsed_addresses.json"):
            results = AddressParser.parse()
            print(results, "Please restart the program.")
            exit(1)

    def walmartAddress(self):
        pass


if __name__ == "__main__":
    scraper = Scraper()
    scraper.parse_zipCode()
