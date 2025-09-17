#find minimum radius of the sprinkler findsmallestrofsprinkler.py

inp =  input("enter array of houses seperataed by spaces")
inp1 = input("enter array of sprinklers seperataed by spaces")

houses = list(map(int,inp.split()))
sprinkler = list(map(int,inp1.split()))

hnum=len(houses)
snum=len(sprinkler)


#comlpexity is n*r
# r=0
# i=0
# j=0

# while(1):
# 	if(sprinkler[j]-r <= houses[i] <= sprinkler[j]+r):
# 		i=i+1
# 	else:
# 		j=j+1

# 	if(i!=hnum and j==snum):
# 		r=r+1
# 		j=0
# 	elif(i==hnum):
# 		print("yayy! your society is greenage if radius:",r)
#		break


#complexity is nlogr
i=0
j=0
loop1=0
loop2=0
if (houses[hnum-1]<=sprinkler[0]):
	midrad=(sprinlkler[0]-houses[0])
	loop1=1
elif (houses[0]>=sprinkler[snum-1]):
	midrad=(houses[hnum-1]-sprinkler[snum-1])
	loop2=1
else:
	minrad=0
	maxrad=max(houses[hnum-1],sprinkler[snum-1])
	midrad=(minrad+maxrad)//2

# while (not loop1 and not loop2):
# 	i = 0
# 	j = 0
# 	r = midrad
# 	satisfied = False
# 	while (1):
# 		if(sprinkler[j]-r <= houses[i] <= sprinkler[j]+r):
# 			i=i+1
# 		else:
# 			j=j+1

# 		if(i!=hnum and j==snum):
# 			r=r+1
# 			j=0
# 		elif(i==hnum):
# 			satisfied = True
# 			break
# 	if satisfied:
# 		maxrad = midrad
# 		midrad = (minrad + maxrad) // 2
# 	else:
# 		minrad = midrad + 1
# 		midrad = (minrad + maxrad) // 2
# 	if (minrad >= maxrad):
# 		break


while(not loop1 and not loop2):
	if(minrad<maxrad):
		#print(minrad, maxrad, midrad)
		if(sprinkler[j]-midrad <= houses[i] <=sprinkler[j]+midrad):
			i=i+1
		else:
			j=j+1
		if(i==hnum):
			maxrad=midrad
			i=0
			j=0
			midrad=(minrad+maxrad)//2
		elif(j==snum):
			minrad=midrad+1
			j=0
			i=0
			midrad=(minrad+maxrad)//2
	else:
		break
print("yayy! your society is greenage if radius:",midrad)


