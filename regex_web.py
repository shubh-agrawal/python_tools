import re
import urllib

num=[]
hand=urllib.urlopen('http://python-data.dr-chuck.net/comments_42.xml')

for line in hand:
	line=line.rstrip()
	num=num+re.findall('[0-9]+',line)

print num	