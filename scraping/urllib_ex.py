#웹 스크래이핑(크롤링)
#import urllib.request
from urllib import request

url = "https://www.naver.com"
contents = request.urlopen(url)
print(contents.read())
