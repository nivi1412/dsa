#O(n*logh)findwoodheightlesscomplexity.py

inp=input("enter the wood heights sep with spaces")
Arr=list(map(int,inp.split()))
wood=int(input("enter the required wood"))

mini=0
maxi=max(Arr)

if wood==0:
    print("cut at height:",maxi)
    break
if wood == sum(Arr):
    print("cut at height:",0)
    break



while(mini<maxi-1):
    else:
        mid = (maxi+mini)//2
        # print("mid:",mid)
        count=0
        for j in range(0,len(Arr),+1):
            # print("diff Arr[j]",Arr[j],"-","Arr[mid]",mid)
            if(Arr[j]-mid>0):
                count=count+(Arr[j]-mid)
        # print("woodcount:",count)
        if(count==wood):
            print("cut at height:",mid)
            break
        elif(count>wood):
            mini=mid
        elif(count<wood):
            maxi=mid
if count!=wood:
    print("-1")

            
