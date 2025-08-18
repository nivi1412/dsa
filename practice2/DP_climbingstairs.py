#DP_climbingstairs.py

def climbing_stirs(stairs,my_dict):
	print("my_dict",my_dict)
	if stairs in my_dict:
		return my_dict[stairs]
	else:
		my_dict[stairs]=climbing_stirs(stairs-1,my_dict)+climbing_stirs(stairs-2,my_dict)
		return my_dict[stairs]

stairs=int(input("enter the number of stairs: "))
my_dict={}
if stairs==0:
	print("enter the valid no of stairs")
else:
	my_dict[1]=1
	my_dict[2]=2
	climbing_stirs(stairs,my_dict)

print(my_dict[stairs])