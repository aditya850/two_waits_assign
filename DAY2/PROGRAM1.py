def OddEven(n):
	if n % 2==0 :
		return True
	else :
	    return False

def Prime(N):
	a = 2
    k = N // 2
    while k >= a:
        if N % a == 0:
            return False
        a += 1
        k = N // a
    return True

def palin(n):
	 N = str(n)
    L = len(N)
    for i in range(L // 2):
        if N[i] != N[L - 1 - i]:
            return False
    return True

def Arms(num):
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10
        sum += digit ** 3  
        temp //= 10  
    if num == sum:  
        return True 
    return False

def check():
	nu=int(input("Enter the number: "))
	if(OddEven(nu)):
		print("EVEN NUMBER")
	else:
	    print("ODD NUMBER")
	if(Prime(nu)):
	    print("PRIME NUMBER")
	if(palin(nu)):
	    print("PALINDROME NUMBER")
	if(Arms(nu)):
	    print("ARMSTRONG NUMBER")

check()	        	


