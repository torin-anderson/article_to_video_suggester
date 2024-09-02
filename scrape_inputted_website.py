# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup


def scrape():
    
    url = 'https://www.mathsisfun.com/calculus/introduction.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print(title)
    print(text)
    print(link)
    # print(soup)



if __name__ == '__main__':
    scrape()