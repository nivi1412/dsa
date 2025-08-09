#graph20.py
#keys and rooms

import ast

def visited_all_rooms(my_dict,visited,key):
	for next_key in my_dict[key]:
		if visited[next_key]==False:
			visited[next_key]=True
			visited_all_rooms(my_dict,visited,key)
	return

rooms=input("enter the rooms list:")
rooms=ast.literal_eval(rooms)

my_dict={}
visited={}
is_visited=True

for i in range(len(rooms)):
	my_dict[i]=rooms[i]
	visited[i]=False
print("graph",my_dict)
visited[0]=True
visited_all_rooms(my_dict,visited,0)
for key,values in visited.items():
	if values==False:
		is_visited=False
		print(False)
		break
if is_visited:
	print(True)
