#Linkedlist_print_append.py

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linkedlist:
	def __init__(self):
		self.head=None

	def prepend(self,data):
		new_node=Node(data)
		if not self.head:
			self.head=new_node
			return

		local=self.head
		self.head=new_node
		new_node.next=local

	def append(self,data):
		new_node=Node(data)
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
			print(current.data,end="->")
			current=current.next
		print("None")

	def delete(self,data):
		data=data
		current=self.head
		if current and current.data==data:
			self.head=current.next
			current=None
			return
		prev = None
		while current and current.data!=data:
			prev=current
			current=current.next
		if current is None:
			return
		prev.next=current.next
		current=None


	def search(self,data):
		data=data
		current=self.head
		while current:
			if data==current.data:
				print(True) 
				return
			current=current.next
		print(False)

	def kth_element(self,index):
		current=self.head
		index=index
		count=0
		while current:
			if count==index:
				return current.data
			count+=1
			current=current.next
		return (-1)

		#O(n ** 2)
	# def reverse(self):
	# 	rll = Linkedlist()
	# 	current_ll=self.head
	# 	count=0
	# 	print(count)
	# 	print(current_ll)
	# 	while current_ll:
	# 		count+=1
	# 		current_ll=current_ll.next
	# 	print(count)
	# 	for i in range(count-1,-1,-1):
	# 		rll.append(ll.kth_element(i))
	# 	return rll

	def reverse(self):
		rll=Linkedlist()
		current_ll=self.head
		while current_ll:
			rll.prepend(current_ll.data)
			current_ll = current_ll.next
		return rll


ll=Linkedlist()
ll.append(1)
ll.append(4)
ll.append(3)
ll.append(12)
ll.prepend(0)
ll.print()
ll.search(5)
ll.search(3)
ll.search(12)
ll.delete(3)
ll.print()
print(ll.kth_element(0))
print(ll.kth_element(1))
print(ll.kth_element(2))
print(ll.kth_element(3))
print(ll.kth_element(4))
print(ll.kth_element(5))
rll = ll.reverse()
ll.print()
rll.print()