#binarysearch4.py
#find the min radius of sprinkler

nh=int(input("enter the number of houses:"))
houses=list(map(int,input("enter house locations:").split()))
ns=int(input("enter the number of sprinklers:"))
sprinklers=list(map(int,input("enter sprinkler locations:").split()))

i=0
j=0
loop1=0
loop2=0
if houses[0]>=sprinklers[ns-1]:
	midrad=houses[nh-1]-sprinklers[ns-1]
	loop1=1
elif houses[nh-1]<=sprinklers[0]:
	midrad=sprinklers[0]-houses[0]
	loop2=1
else:
	minrad=0
	maxrad=max(sprinklers[ns-1],houses[nh-1])
	midrad=(minrad+maxrad)//2

while((not(loop1 and loop2))):
	if ()

\
?
