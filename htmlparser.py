import urllib
from bs4 import BeautifulSoup

url = raw_input("Enter - ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup.find_all('a')

for tag in tags:
    print tag.get('href', None)
