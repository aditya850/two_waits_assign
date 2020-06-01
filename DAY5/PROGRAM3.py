num=int(input("enter the number of house: "))
print("ENTER THE VALUE ONE BY ONE")
List=[]
for i in range(num):
	List.append(input())

def House(List):
    if len(List) == 2:
        return max(List)
    if len(List) == 1:
        return List[0]
    if len(List) == 3:
        return max(List[1], List[0] + House(List[2:]))
    return max(List[1] + House(List[3:]), List[0] + House(List[2:]))

    print("The maximum stolen value from Houses is", House(List))

