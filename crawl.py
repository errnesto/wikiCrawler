import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class Crawler:

  def __init__(self):
    self.f       = open('workfile.txt', 'w')
    self.urlBase = "http://en.wiktionary.org"
    self.url     = "/w/index.php?title=Category:German_nouns"



  def parsePage(self):
    # download and parse file
    response = urllib.request.urlopen(self.urlBase + self.url)
    document = BeautifulSoup(response)

    # extract links from file
    liList = document.find(id='mw-pages').find_all('div', {'class': 'mw-content-ltr'})
    for div in liList:
      for li in div.find_all('li'):
        self.f.write(li.string + '\n')

    links    = document.find_all('a', {'title': 'Category:German nouns'})
    linkElem = links[0]

    if linkElem:
      self.url = linkElem['href']
    else:
      self.url = False

  def goThroughPager(self):
    while self.url:
      self.parsePage()


c = Crawler()
c.goThroughPager()