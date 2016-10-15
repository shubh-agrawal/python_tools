import urllib
import xml.etree.ElementTree as ET
data=""
sum=0

website=raw_input("Enter the website:")
handle=urllib.urlopen(website)

for line in handle:
	line=line.rstrip()
	data=data+line

tree=ET.fromstring(data)

lst=tree.findall('.//count')
for item in lst:
	sum=sum+int(item.text)

print "count :",len(lst)
print "sum: ",sum