#twopointer1.py
#a[i]-b[i]=c sorted array as inp

#O(nlogn)

# def binarysearch(a,p,r,inp):
# 	while (p<=r):
# 		q=(p+r)//2
# 		#print(p,q,r)
# 		if inp[q]==a:
# 			return inp[q]
# 		elif inp[q]<=a:
# 			p=q+1
# 		elif inp[q]>a:
# 			r=q-1
# 		else:
# 			return -1



# inp=input("enter the array values seperated by spaces:")
# inp=list(map(int,inp.split()))

# diff=int(input("enter the difference"))

# for i in range(len(inp)):
# 	a=diff+inp[i]
# 	p=0
# 	r=len(inp)-1
# 	b=binarysearch(a,p,r,inp)
# 	if (b!=None):
# 		print(inp[i],b)

#O(n)

inp=input("enter the array values seperated by spaces:")
inp=list(map(int,inp.split()))
diff=int(input("enter the difference"))

p=0
r=0

while(r<=(len(inp)-1)):
	#print(inp[p],inp[r])
	if (inp[r]-inp[p] == diff):
		print(inp[p],inp[r])
		p+=1
		r+=1

	elif (inp[r]-inp[p])>diff:
		p+=1
		#r+=1
	elif((inp[r]-inp[p])<diff):
		r+=1



		

