str1=input("ENTER THE STRING: ")
str2=""
for i in str1:
	if i not in str2:
		str2 += i
print("AFTER REMOVING: ",str2)
