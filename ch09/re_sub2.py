
import re

data = '''
kim = 861122-1894343
lee = 890212-2493445
'''

pat = re.compile("(\d+)-\d+")
print(pat.sub("\g<1>-*******",data))
