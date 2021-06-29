

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page<max_pages:
        url = 'https://www.trademap.org/Index.aspx?nvpm=' + str(page)
            
        
