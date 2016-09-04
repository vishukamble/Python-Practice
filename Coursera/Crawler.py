# __author__ = Vishu Kamble

import urllib
from BeautifulSoup import *
url = 'http://python-data.dr-chuck.net/known_by_Yakup.html'
count = input("Enter Count: ")
pos = input("Enter position: ")

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos-1].get('href')
    print ("Retrieving: " + str(url))

print (url.split('known_by_')[1])