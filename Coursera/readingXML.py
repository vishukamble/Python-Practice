import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_215188.xml'
data = urllib.urlopen(url).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment/count')
result = 0
for count in lst:
    result += int(count.text)

print 'Sum: ', result