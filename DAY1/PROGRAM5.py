p1=float(input("ENTER THE SCORE OF Ist PLAYER(60-BALLS): "))
p2=float(input("ENTER THE SCORE OF IInd PLAYER(60-BALLS): "))
p3=float(input("ENTER THE SCORE OF IIIrd PLAYER(60-BALLS): "))
s1=(p1/60)*100
s2=(p2/60)*100
s3=(p3/60)*100
max1=int(p1/6)
max2=int(p2/6)
max3=int(p3/6)
runs1=(60*s1)/100+p1
runs2=(60*s2)/100+p2
runs3=(60*s3)/100+p3
print("ABOUT PLAYER1:")
print("STRIKE RATE: ",s1)
print("EXPECTED RUNS: ",runs1)
print("MAX SIXES(6's): ",max1)
print("ABOUT PLAYER2:")
print("STRIKE RATE: ",s2)
print("EXPECTED RUNS: ",runs2)
print("MAX SIXES(6's): ",max2)
print("ABOUT PLAYER3:")
print("STRIKE RATE: ",s3)
print("EXPECTED RUNS: ",runs3)
print("MAX SIXES(6's): ",max3)
