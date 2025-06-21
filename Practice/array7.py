#array7.py
#1.find intersection given arrays
#2.count repleasted and unique elemnts of 2 arrays

def commonarray(A1,A2):
	i=0
	j=0
	nA1=len(A1)
	nA2=len(A2)
	result=[]

	while(i<nA1 and j<nA1):
		if A1[i]==A2[j]:
			result.append(A1[i])
		i+=1
		j+=1
	return result



A1=list(map(int,input("enter 1 st array sep by spaces:").split()))
A2=list(map(int,input("enter 2 nd array sep by spaces:").split()))
uniq_count=0
rep_count=0
print(commonarray(A1,A2))
for i in A1:
	if i not in A2:
		uniq_count+=1
	else:
		rep_count+=1
print(uniq_count)
print(rep_count)