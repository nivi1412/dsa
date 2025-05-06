#stringwave.py

inp=input("enter the string:")
row=int(input("enter number of rows:"))

for i in range(row):
	row[i]=''
p=0
q=1
r=2
if len(inp)==1:
	row[0]=inp[0]

elif len(inp)==2:
	row[0]=inp[0]
	row[1]=inp[1]

else:
	for i in range(len(inp)/3):
		row[p]=inp[p]
		row[q]=inp[q]
		row[r]=inp[r]

		if(p!= len(inp)):
			p+=1
		if(q!=len(inp)):
			q+=1
		if(r!=len(inp)):
			r+=1
print(row[0])
print(row[1])
print(row[2])



