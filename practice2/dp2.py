#dp2.py

def genparan(n,out,oc,cc,string):

	if len(string)==2*n:
		out.append(string)
	if oc<n:
		genparan(n,out,oc+1,cc,string+"(")
	if cc<oc:
		genparan(n,out,oc,cc+1,string+")")


n=int(input("enter the paranthesis count: "))
out=[]
genparan(n,out,0,0,"")

print(out)