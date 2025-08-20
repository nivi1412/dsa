#graphpractice_course_schedule.py
# Course Schedule (Topological Sort / Cycle Detection)

# Problem:
# You are given numCourses and a list of prerequisites, where each pair [a, b] means to take course a you must first take course b.
# Return True if you can finish all courses, otherwise False.

import ast

def detect_cycle(node,my_dict,visited,finished):
	is_cycle=False
	for next_node in my_dict[node]:
		print("2.nextnode:",next_node)
		if finished[next_node]==False and visited[next_node]==True:
			return True
		if visited[next_node]==False:
			visited[next_node]=True
			is_cycle=is_cycle or detect_cycle(next_node,my_dict,visited,finished)
	finished[node]=True
	return is_cycle

courses=input("enter the course list: ")
courses=ast.literal_eval(courses)

my_dict={}
visited={}
finished={}
cycle_detected=False
for course in courses:
	if course[1] not in my_dict:
		my_dict[course[1]]=[]
		visited[course[1]]=False
		finished[course[1]]=False
	if course[0] not in my_dict:
		my_dict[course[0]]=[]
		visited[course[0]]=False
		finished[course[0]]=False
	my_dict[course[1]].append(course[0])
print(my_dict)
for node in my_dict:
	print("1.node:",node)
	if visited[node]==False:
		visited[node]=True
	cycle=detect_cycle(node,my_dict,visited,finished)
	if cycle:
		cycle_detected=True
		break
if cycle_detected:
	print(False)
	print("all courses are not completed")
else:
	print(True)
	print("all courses are completed")


