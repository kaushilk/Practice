# scraping exercise. pulling the Dow jones companies (top 30 companies)

import requests
from bs4 import BeautifulSoup


page = requests.get('https://www.marketwatch.com/investing/index/djia')
soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='table__row')
last_links.decompose()
# find div section
div_section = soup.find(class_='element element--table IndexScreenerLeaders')
# narrow down to individual info
stock_list = div_section.find_all('a')
stock_change = div_section.find_all('bg-quote')
i = 0
for stock in stock_list:
    names = stock.contents[0]
    last_price = stock_change[i].contents[0]
    i+= 1
    change = stock_change[i].contents[0]
    i+= 1
    p_change = stock_change[i].contents[0]
    i+= 1

    print(names)
    print("Last: " + last_price)
    print("Change: " + change)
    print("% Change:" + p_change + "\n")
