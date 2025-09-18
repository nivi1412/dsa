#power of an integer

def Pow(n,p):

	if p == 0:
		return 1

	elif p == 1:
		return n

	elif(p%2==0):
		i=p//2
		j=p//2
	else:
		i=p//2
		j=p//2+1

	return Pow(n,i)*Pow(n,j)


n=int(input("enter the base:"))
p=int(input("enter the power:"))

Product =1

Product=Product * Pow(n,p)
print(Product)
