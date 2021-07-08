from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://finance.naver.com/marketindex/")
contents = BeautifulSoup(html.read().decode('euc-kr','replace').encode('utf-8','replace'),'html.parser')
market = contents.find('div',{'class':'market_data'})
ma = market.find_all('li')
for li in ma:
    ex = li.find('span',{'class':'blind'})
    val = li.find('span',{'class':'value'})
    # print("종목{} : {}원".format(ex.text,val.text))
    print(ex.string.split(' ')[-1] ,':',val.string)