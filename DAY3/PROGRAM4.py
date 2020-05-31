n=int(input("ENTER THE NO OF ELEMENT: "))
print("ENTER ITEM ONE BY ONE: ")
List = []
for i in range(n):
	List.append(input())

def dup(List):
	List1=[]
	for i in List:
		if i not in List1:
			List1.append(i)
	return List1

print("AFTER REMOVING DUPLICATE LIST: ",dup(List))