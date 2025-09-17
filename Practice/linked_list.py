#linkedlist.py
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
	def prepend(self,data):
		new_node=node(data)
		if not self.head:
			self.head=new_node
			return

		new_node.next=self.head
		self.head=new_node

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
	def search(self,val):
		current=self.head
		while current:
			if current.data==val:
				print(1)
				return
			current=current.next
		print(-1)

	def reverse(self):
		rll=linkedlist()
		current=self.head
		while current:
			rll.prepend(current.data)
			current=current.next
		return rll



ll=linkedlist()
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(10)
ll.print()
ll.prepend(1)
ll.print()
ll.delete(2)
ll.print()
ll.search(10)
ll.search(11)
ll.reverse().print()

