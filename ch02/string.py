#문자열 안에 인용부호(작은,큰따옴표) 포함할 때

sentence = "'힘내세요!' 라고 말했습니다."
print(sentence)

say = '"Python is very easy." he says'
print(say)

#여러줄로 문자 출력하기

hook ="""
무궁화 삼천리 화려강산
대한사람 대한으로 깊이 보전하세
"""

song1 = """
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
"""
print(song1 + hook)

song2 = '''
남산 위에 저 소나무 철갑을 두른듯
바람 서리 불변함은 우리 기상일세
'''

print(song2 + hook)
