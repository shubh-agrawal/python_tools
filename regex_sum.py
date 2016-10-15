import re
numlist=[]
sum=0

hand=open('regex_sum_270310.txt')
for line in hand:
	line=line.rstrip()
	numlist=numlist+re.findall('[0-9]+',line)

print numlist

for i in range(0,len(numlist)):
	sum=sum+int(numlist[i])

print sum





