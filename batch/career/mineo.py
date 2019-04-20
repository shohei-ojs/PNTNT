from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import urllib.request
from career.base import Career

class Mineo(Career):
  url = ""

  def __init__(self, url):
    self.url = url

  def Scraping(self):
    with urllib.request.urlopen(self.url) as respones:
      html = respones.read()
    soup = BeautifulSoup(html)
    with open("temp/mineo.html", mode='w') as f:
      f.write(str(soup.find_all(class_="container-price")))

    print(soup)