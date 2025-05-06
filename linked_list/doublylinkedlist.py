#doublylinkedlist.py
# append, print, prepend,search, kth element,reverse

class Node():
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
class linkedlist():
	def __init__(self):
		self.head=None

	def append(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
			return
		current=self.head
		while current.next:
			current=current.next
		current.next=new_node
		new_node.prev=current

	def display_forward(self):
		current=self.head
		while current:
			print(current.data,end="<->")
			current=current.next
		print("None")

	def display_backward(self):
		current=self.head
		while current.next:
			current=current.next
		while current:
			print(current.data,end="<->")
			current=current.prev
		print("None")

	def prepend(self,data):
		new_node=Node(data)
		current=self.head
		new_node.next=current
		current.prev=new_node
		self.head=new_node

	def search(self,data):
		current=self.head
		while current:
			if current.data==data:
				print("True")
				return
			current=current.next
		print("False")

	def kth_element(self,index):
		current=self.head
		i=0
		while current:
			if i==index:
				return current.data
			i+=1
			current=current.next
		return(-1)
			
	def reverse(self):
		current=self.head
		rdll=linkedlist()
		while current.next:
			current=current.next
		while current:
			rdll.append(current.data)
			current=current.prev
		return rdll

	def delete(self,data):
		current=self.head

		while current:
			if current.data==data:
				if current.prev is None:
					self.head=current.next
					if self.head:
						self.head.prev=None
				else:
					current.prev.next=current.next
					if current.next:
						current.next.prev=current.prev
				return
			current=current.next


inp=input("enter number seperated by space:")
num=list(map(int,inp.split()))
dll=linkedlist()
for i in num:
	dll.append(i)
dll.display_forward()
dll.display_backward()
dll.prepend(0)
dll.display_forward()
dll.display_backward()
dll.search(4)
dll.search(5)
dll.search(10)
print(dll.kth_element(0))
print(dll.kth_element(4))
print(dll.kth_element(10))
rdll=dll.reverse()
rdll.display_forward()
dll.delete(4)
dll.delete(0)
dll.display_forward()



























































