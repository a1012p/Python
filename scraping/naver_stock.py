from urllib import request
from bs4 import BeautifulSoup

def getcontent():
    url = "https://finance.naver.com/item/main.nhn?code=005930#"
    html = request.urlopen(url)
    contents = BeautifulSoup(html,'html.parser')
    return contents

cont = getcontent()
no_today = cont.find('p',{'class':'no_today'})
price = no_today.find('span',{'class':'blind'}) #blind는 웹에서 보이지 않음
print(price.text)
print("삼성전자 주가 : {}원".format(price.text))