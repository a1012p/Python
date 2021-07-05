# BeautifulSoup 모듈 사용하기

from bs4 import BeautifulSoup

html ="""
<html>
<body>
    <ul class ='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로봇</li>
    </ul>
    <ul class ='lang'>
        <li>한국어</li>
        <li>중국어</li>
        <li>영어</li>
    </ul>
</body>
</html>
"""

contnents = BeautifulSoup(html , 'html.parser')
ul = contnents.find("ul",{'class':'lang'})
# print(ul)
# li = ul.find('li')
# print(li)

lis = ul.find_all('li')
print(lis)
print(lis[1].text)