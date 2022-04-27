import numpy as np
import urllib.request 
from bs4 import BeautifulSoup


url = 'https://jmagazine.joins.com/forbes/view/333975'

conn = urllib.request.urlopen(url) # art_eco = conn.read() 
soup = BeautifulSoup(conn, "html.parser")


objects = soup.find_all('b', class_='artsub_title')

name40 = []

for i in objects:
    name40.append(i.text[3:])
# print(objects[0].text)

name40 = np.asarray(name40)
print(name40)

np.savetxt('40names.txt', name40, fmt='%s', encoding='UTF-8')
