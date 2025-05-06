#find maximum radius of the sprinkler maxradiusofsprinkler.py order(n square)
#import bisect


hnum = int(input("enter the number of houses:"))
snum = int(input("enter the number of sprinklers: "))

inp =  input("enter array of houses seperataed by spaces")
inp1 = input("enter array of sprinklers seperataed by spaces")

radious = int(input("enter the radious"))

houses = list(map(int,inp.split()))
sprinkler = list(map(int,inp1.split()))

#bruteforce O(n square)
# count=0
# for i in houses:
# 	for k in sprinkler:
# 		diff=k-radious
# 		summ=k+radious
# 		if diff<0:diff=0
# 		if diff<=i<=summ:
# 			count=count+1
# 			break

#O(n.logn) dont take all the values of sprinkler find upper and lower bound
# count =0 
# for i in range(len(houses)):
# 	lb=bisect.bisect_left(sprinkler,houses[i])
# 	ub=bisect.bisect_right(sprinkler,houses[i])
# 	print(lb,ub)
# 	if (ub > snum - 1):
# 		ub = ub - 1
# 	if (lb > snum - 1):
# 		lb = lb - 1
	
# 	if sprinkler[lb] > houses[i] && lb > 0:
# 		lb=ub-1
# 	print(lb,ub)
# 	print("sprinkler[lb]",sprinkler[lb])
# 	print("sprinkler[ub]",sprinkler[ub])
# 	difflb=sprinkler[lb]-radious
# 	diffub=sprinkler[ub]-radious
# 	if difflb<0:
# 		difflb=0
# 	if diffub<0:
# 		diffub=0

# 	if(difflb<= houses[i] <= sprinkler[lb]+radious or difflb <= houses[i] <= sprinkler[ub]+radious ):
# 		count=count+1
# 		print(count)

# O(n)solution:

#keep pointer p and q each at start of the arrays for each sprinkler check the house is covered within the radious

i=0
j=0

while (1):
	print(i,j)
	if(sprinkler[j]-radious <= houses[i] <= sprinkler[j]+radious):
		i=i+1
	else:
		j=j+1

	if(i!=hnum and j==snum):
		print("there is draught and greenary in your society")
		break
	elif(i==hnum):
		print("yayy! your society is greenage")
		break






