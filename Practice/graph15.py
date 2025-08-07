#graph15.py
#Network Delay Time

def network_delay_time(start_node,times,visited):
	times=0
	for j in range(len(times[0])):
		next_node=times[j][1]
		times=times+times[j][2]
		if visited[next_node]==False:
			visited[next_node]==True
			network_delay_time(next_node,times,visited)


n=int(input(" enter no of nodes: "))
k=int(input(" enter the start_node: "))
rows=int(input(" enter row length of times matrix: "))
cols=int(input(" enter col length of times matrix: "))

times=[]
for i in range(rows):
	inp=input(f"enter the values if row {row+1} : ")
	times.append(list(map(int,inp.split())))

visited=[False for _ in range(n)]

for i in range(rows):
	if visited[times[i][0]]==False:
		visited[times[i][0]]=True
		start_node=times[i][0]
		network_delay_time(start_node,times,visited)
