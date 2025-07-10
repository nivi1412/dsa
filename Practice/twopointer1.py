#twopointer1.py
#a[i]-b[i]=c sorted array as inp

#O(n logn)
# def binarysearch(Arr,a,p,r):
# 	while(p<=r):
# 		q=(p+r)//2
# 		print(p,r,Arr[q],a)
# 		if Arr[q]==a:
# 			return q
# 		elif Arr[q]>a:
# 			r=q-1
# 			binarysearch(Arr,a,p,r)
# 		elif Arr[q]<a :
# 			p=q+1
# 			binarysearch(Arr,a,p,r)
# 	return -1

# Arr=input("enter the sorted array:")
# Arr=list(map(int,Arr.split()))
# C=int(input("enter the difference"))

# for i in range(len(Arr)):
# 	a=Arr[i]+C
# 	p=0
# 	r=len(Arr)-1
# 	j=binarysearch(Arr,a,p,r)
# 	if j!=-1:
# 		print("pair is :",Arr[i],Arr[j])
# 		break
# 	if j==-1:
# 		continue

#O(n)

Arr=input("enter the sorted array:")
Arr=list(map(int,Arr.split()))
C=int(input("enter the difference"))

p=0
r=0
while(r<=len(Arr)-1):
	if Arr[p]-Arr[r]==C:
		print(Arr[p],Arr[r])
		p+=1
		r+=1
	elif Arr[p]-Arr[r]<C:
		p+=1
	elif Arr[p]-Arr[r]>C:
		r+=1









