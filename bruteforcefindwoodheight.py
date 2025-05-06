#bruteforcefindwoodheight.py

inp=input("enter the wood heights sep with spaces")
Arr=list(map(int,inp.split()))
wood=int(input("enter the required wood"))

maximum=Arr[0]
for i in Arr:
    if(i >maximum):
        maximum=i
for i in range(maximum,0,-1):
    count=0
    for j in range(0,len(Arr),+1):
        print(i,Arr[j])
        if(Arr[j]-i>0):
            count=count+(Arr[j]-i)
    if(count==wood):
        print("wood should be cut at height",i,"to get wood count", count)
        break

       