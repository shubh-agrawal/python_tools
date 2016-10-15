p=[]
world=['green','red','red','green','green']
Z="red"
pHit=0.6
pMiss=0.2
n=5


for i in range(n):
	p.append(1./5)

def sense(p,Z):
	"sensor for color"
	q=[]
	flag=1
	for i in range(n):
		if (world[i]==Z):
			flag=pHit
		else: 
			flag=pMiss
		q.append(p[i]*flag)
	return q	

q=sense(p,Z)

for i in range(n):
	p[i]=q[i]/sum(q)

print p