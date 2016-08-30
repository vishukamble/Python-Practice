import random
import urllib.request

def download_img(url):
    name = random.randrange(1,10000)
    fullname = str(name) + '.jpg'
    urllib.request.urlretrieve(url, fullname)

download_img('https://geekstarts-pc2ufbdctbrttjiddn1higshzrabrvap.netdna-ssl.com/wp-content/uploads/2014/09/julianassange9-mytrickytricks-blogspot-com.jpg')
