import requests
import os
from urllib.request import urlretrieve
# data = {'firstname': '莫烦', 'lastname': '周'}
# r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
# print(r.text)
os.makedirs('./img/',exist_ok=True)
IMAGE_URL="https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
#
urlretrieve(IMAGE_URL,'./img/image1.png')

#'w' is for text file only
r=requests.get(IMAGE_URL)
with open('./img/image2.png','wb')as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(r.content)
