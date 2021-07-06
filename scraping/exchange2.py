from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("https://finance.naver.com/marketindex/")
contents = BeautifulSoup(html.read().decode('euc-kr','replace').encode('utf-8','replace'),'html.parser')
lis =contents.select('ul.data_lst li')

for li in lis:
    ex = li.select_one('span.blind')
    val = li.select_one('span.value')
    # print("종목{} : {}원".format(ex.text,val.text))
    print(ex.string.split(' ')[-1] ,':',val.string)