# Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B. 
# You should preserve the original relative order of the nodes in each of the two partitions. 
# Input 1: 
# A = [1, 4, 3, 2, 5, 2]
# B = 3
# Input 2: 
# A = [1, 2, 3, 1, 3]
# B = 2
# Output 1: 
# [1, 2, 2, 4, 3, 5]
# Output 2: 
# [1, 1, 2, 3, 3]
# Explanation 1:
# [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
# Explanation 2:
# [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linkedlist:
	def __init__(self):
		self.head=None

	def prepend(self,data):
		new_node=Node(data)
		new_node.next=self.head
		delf.head=new_node


	def append(self,data):
		new_node=Node(data)
		last=self.head
		if self.head is None:
			self.head=new_node
			return
		while last.next:
			last=last.next
		last.next=new_node

	def print(self):
		current=self.head
		while current:
			print(current.data,end="->")
			current=current.next
		print("None")

	def concat(self,grt_ll):
		great=grt_ll.head
		less=self.head
		if self.head is None:
			self.head=great.head
			return
		while less.next:
			less=less.next
		less.next=great


def concat_two_lists(less_ll, grt_ll):
	# concat logic
	return less_ll

inp=input("enter the elements of linked list seperated by spaces:")
A=list(map(int,inp.split()))
B=int(input("enter the number:"))
less_ll=Linkedlist()
grt_ll=Linkedlist()
for i in A:
	if i>=B:
		grt_ll.append(i)
	else:
		less_ll.append(i)
less_ll.concat(grt_ll)
less_ll.print()
# grt_ll.print()
# less_ll.print()












