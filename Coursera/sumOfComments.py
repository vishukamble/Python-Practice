# __author__ = Vishu Kamble


import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_215191.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
s = 0
tags = soup('span')
for tag in tags:
    s += int(tag.contents[0])

print s