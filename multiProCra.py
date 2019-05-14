import multiprocessing as mp 
import time 
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup
import re

base_url='https://movanzhou.github.io/'

def crawl(url):
    response=urlopen(url)
    return response.read().decode()

def parse(html):
    soup=BeautifulSoup(html,'lxml')
    urls=soup.find_all('a',{"href":re.compile('^/.+?/$')})
    title=soup.find('h1').get_text().strip()
    #reduce repeat
    page_urls=set([urljoin(base_url,url['href'])for url in urls])
    url=soup.find('meta',{'property':"og:url"})['content']
    return title,page_urls,url

unseen=set([base_url,])
seen=set()