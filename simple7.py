from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve

os.makedirs('./geoimg/',exist_ok=True)

URL="http://www.nationalgeographic.com.cn/animals/"
html=requests.get(URL).text
soup=BeautifulSoup(html,features="lxml")

img_ul=soup.find_all("ul",{"class":"img_list"})
for ul in img_ul:
    imgs=ul.find_all('img')
    for img in imgs:
        url=img['src']
        r=requests.get(url,stream=True)
        image_name = url.split('/')[-1]
        with open('./geoimg/%s'%image_name,'wb')as f:
           for chunk in r.iter_content(chunk_size=128):
              f.write(r.content)
              print('Saved %s'% image_name)
