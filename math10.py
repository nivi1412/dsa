#math10.py
#find all the n digits number combinations in the given array


#combinations less than i
def combinationlessthan(A,i,C_digit,C):
	count=[]
	loopcount1=0
	loopcount2=1
	original,_=numdigits(C)
	if original == len(C_digit):
		flag=True
	else:
		flag=False
	while(i>=0):
		if i==len(C_digit)-1:
			for j in A:
				if j<C_digit[i] and j!=0 and flag:	# j!=0 only for first digit
					loopcount1+=1
				elif j<C_digit[i] and not(flag):
					loopcount1+=1

			count.append(loopcount1)
		else:
			count.append(len(A))
		
		i-=1
	if len(count) > 0:
		for k in range(0,len(count),+1):
			loopcount2=loopcount2*count[k]
		return loopcount2
	else:
		return 0
				
#combinations equal to
def combinationequalto(A,i,C_digit,C):
	# print("len,i",len(C_digit),i)
	if len(C_digit)!=0:
		if C_digit[i] not in A:
			return 0
		else:
			if i > 0:
				C_digit.remove(C_digit[i])
				return LessthanEqC_Combinations(A, C_digit, i-1,C)
			else:
				return 1
	else: return 0

#Lessthan C combinations
def LessthanEqC_Combinations(A,C_digit,i,C):
	localcount=0
	finalcount=0
	localcount=combinationlessthan(A,i,C_digit,C)
	finalcount=finalcount+localcount
	print("finalcount1:",finalcount)
	finalcount2=combinationequalto(A,i,C_digit,C)
	finalcount=finalcount+finalcount2
	print("finalcount2:",finalcount)
	return finalcount

#total combinations
def total_Combinations(A):
	Zero_count=0
	for i in A:
		if i==0:
			Zero_count+=1

	if Zero_count==0:
		totalcount=length**B
		return totalcount
		#print("no of digits=",totalcount)
	else:
		totalcount=((length-Zero_count)*(length**(B-1)))
		return totalcount
		#print("no of digits=",totalcount)


def numdigits(C):
	digit=[]
	count=0
	while(C>0):
		digit.append(C%10)
		C=C//10
		count+=1
	return(count,digit)


inp=input("enter the numbers of array followed by spaces:")
A=list(map(int,inp.split()))
B=int(input("enter the number of digits:"))
C=int(input("enter the max digit:"))

C_len,C_digit=numdigits(C)
length=len(A)

if B<C_len:
	print(total_Combinations(A))

elif B==C_len:
	i=len(C_digit)-1
	print(LessthanEqC_Combinations(A,C_digit,i,C))

else:
	print("number of digits = 0")



















