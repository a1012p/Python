#웹 스크래이핑(크롤링)
#import urllib.request
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.naver.com"
contents = request.urlopen(url)

soup = BeautifulSoup(contents,'html.parser')
title = soup.find('div',{'class':'service_area'}) # find() 는 맨 처음 나오는 태그만 검색
print(title)
