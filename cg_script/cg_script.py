#urllib doesnt support https hence use urllib2 that supports https


#Given below the block of code can also be used for https
#import httplib
#handle=httplib.HTTPSConnection("erp.iitkgp.ernet.in")
#handle.request("GET","/StudentPerformance/view_performance.jsp?rollno=14ME10052")
#response=handle.getresponse()
#data=response.read()
#print data

import urllib2
import re
import csv
import time
comm="https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno="


def cg_stalker(roll_str_func):
	
	data=""
	compl_str=comm+roll_str_func
	handle=urllib2.urlopen(compl_str)

	for line in handle:
		line=line.strip()
		data=data+line

	name=re.findall('<b>Name.*?<td>(.*?)</td>',data)
	print name[0]

	sgpa_lst=re.findall('SGPA.*?([0.00-9.00]+)</td>',data)
	print sgpa_lst

	cgpa_lst=re.findall('CGPA.*?([0.00-9.00]+)</td>',data)
	if(len(cgpa_lst)>0):
		print cgpa_lst[0]

	if len(sgpa_lst)>0 and len(cgpa_lst)>0:
		f.writerow([name[0],roll_str_func,cgpa_lst[0],sgpa_lst[0]])


input_str=raw_input("Enter year and dept code: ")
file_str=raw_input("Enter output file name: ")
f=csv.writer(open(file_str,"wb"))

f.writerow(["Name","Roll no.","CGPA","SGPA"])
for rn in range(10001,10085,1):
	roll_no_str=input_str+str(rn)
	cg_stalker(roll_no_str)
	time.sleep(0.500)


for rn in range(30001,30055,1):
	roll_no_str=input_str+str(rn)
	cg_stalker(roll_no_str)	
	time.sleep(0.500)





