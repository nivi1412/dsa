#linkedlist3.py
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

from collections import OrderedDict

class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linkedlist:
	def __init__(self):
		self.head=None

	def append(self,data):
		new_node=node(data)

		if not self.head:
			self.head=new_node
			return
		last=self.head
		while last.next:
			last=last.next
		last.next=new_node

	def print(self):
		current=self.head
		while current:
			print(current.data)
			current=current.next

	def count(self):
		current=self.head
		my_dict=OrderedDict()
		count=0
		prev=current
		while current:
			if current.data==prev.data:
				count+=1
			else:
				my_dict[prev.data]=count
				count=1

			prev=current
			current=current.next
		my_dict[prev.data]=count
		return my_dict

	def delete(self,val):
		current=self.head
		prev=None
		while current:
			if current.data==val:
				if prev:
					prev.next=current.next
					current=None
				else:
					self.head=current.next
				return
			else:
				prev=current
				current=current.next

	def remove(self,my_dict):
		current=self.head
		while current:
			if my_dict[current.data]>1:
				ll.delete(current.data)
			current=current.next
			


ll=linkedlist()
A=input("enter elements of linkedlist")
A=list(map(int,A.split()))

for i in A:
	ll.append(i)
my_dict=ll.count()
ll.remove(my_dict)
print(my_dict)
ll.print()