n=int(input("Enter the number: "))
def fabi(a):
	if a==0:
		return 0
	elif a==1:
		return 1
	else:
		return fabi(a-1)+fabi(a-2)

for i in range(n):
	print(fabi(i))

