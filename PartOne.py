#Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a formatted output one currency at a time. 
#The output should display the name of the currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#Finding the Scrappable Website
webpage = 'https://coinmarketcap.com/'
page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(f"{title.text}\n")

#Now we want to get all of the rows in the table and pull out the top 5
table_rows = soup.findAll("tr")

for row in table_rows[1:6]:
    td = row.findAll("td")
    FullName = td[2].text
    capital_indices = [i for i, char in enumerate(FullName) if char.isupper()]
    symbol = capital_indices[1]
    Ticker = FullName[symbol:]
    print(f"Crypto Name and Symbol {FullName}, Ticker: {Ticker}")

    price = td[3].text
    print(f"Current Price: {price}")

    change24 = td[5].text
    print(f"Percent change in 24hrs: {change24}\n") 