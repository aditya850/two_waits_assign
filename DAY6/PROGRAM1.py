str1=input("ENTER THE STRING")
List=list(str1)
x=len(List)
d=0
c=0
for i in range(x):
	
	for x in List:
		c=c+1
	if c==1:
		d=d+1
print("ANSWER IS",d)
