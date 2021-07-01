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
</body>
</html>
"""

soup = BeautifulSoup(html,'html.parser')
# print(soup)
text = soup.find('ul')
print(text)
print(text.text)
print(text.attrs)