#math8.py
#binary to decimal

num=int(input("enter the binary number:"))
decimal=[]
while(num>0):
	quo=num%10
	decimal.append(quo)
	num=num//10
print(decimal)
dec=0
for i in range(len(decimal)):
	dec=dec+decimal[i]*(2**i)
print(dec)
