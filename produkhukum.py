import requests
import os
from bs4 import BeautifulSoup

nametitle = ''
nameurl = ''
namedownload = ''


f = open('lldikti.txt', 'a')
url = "https://www.lldikti4.id/produk-hukum/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
elemt = soup.find_all(['a', 'span'], class_=[
                      "package-title", "__dt_download_count"])


for title in elemt:
    nametitle = title.text
    nameurl = title.get("href")
    f.write(nametitle + '\n' + str(nameurl) + '\n')


f.close()
