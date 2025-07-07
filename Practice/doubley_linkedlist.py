#doubley_linkedlist.py

class node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
class doublylinkedlist:
	def __init__(self):
		self.head=None

	def append(self,data):
		new_node=node(data)

		if not self.head:
			self.head=new_node
			return
		current=self.head
		while current.next:
			current=current.next
		current.next=new_node
		new_node.prev=current

	def print(self):
		current=self.head
		while current:
			print(current.data)
			current=current.next

	def prepend(self,data):
		new_node=node(data)
		current=self.head
		self.head=new_node
		new_node.next=current
		current.prev=new_node

	def delete(self,data):
		current=self.head
		prev=None
		if not self.head:
			return
		while current:
			if current.data==data:
				if current.prev is None:
					self.head=current.next
					if current.next:
						current.next.prev=None

				else:
					current.prev.next=current.next
					if current.next:
						current.next.prev=current.prev
			current=current.next

	def reverse(self):
		current=self.head
		while current.next:
			current=current.next
		while current:
			print(current.data)
			current=current.prev


dll=doublylinkedlist()
dll.append(1)
dll.append(5)
dll.append(7)
dll.append(9)
dll.append(0)
dll.append(10)
dll.print()
dll.delete(10)
dll.print()
dll.reverse()










