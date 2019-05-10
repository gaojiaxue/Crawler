from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html=urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode("utf-8")
soup=BeautifulSoup(html,features="lxml")
all_img=soup.find_all("img",{"src":re.compile('.*?\.jpg')})
for img in all_img:
    print(img['src'])
