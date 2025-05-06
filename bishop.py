#math7.py
#bishop.py

row_max=7
col_max=7
count=0

i=int(input("enter the row position of bishop:"))
j=int(input("enter the col position of bishop"))
k=i
l=j

while(i<row_max and j<col_max):
	i+=1
	j+=1
	count+=1
	print(i,j)
i=k
j=l
while(i<row_max and j>0):
	i+=1
	j-=1
	count+=1
	print(i,j)
i=k
j=l
while(i>0 and j<col_max):
	i-=1
	j+=1
	count+=1
	print(i,j)
i=k
j=l
while(i>0 and j>0):
	i-=1
	j-=1
	count+=1
	print(i,j)
i=k
j=l
print("number of steps:",count)