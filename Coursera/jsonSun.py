# __author__ = Vishu Kamble

import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_215192.json'
data = urllib.urlopen(url).read()
info = json.loads(data)
result = 0
for x in info['comments']:
    result += x['count']

print result