#LL_Palindrome.py

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linkedlist:
	def __init__(self):
		self.head=None

	def prepend(self,data):
		new_node=Node(data)
		current=self.head
		if current == None:
			self.head=new_node
			return
		self.head=new_node
		new_node.next=current
		
	def append(self,data):
		new_node=Node(data)
		if self.head is None:
			self.head=new_node
			return
		last=self.head
		while last.next:
			last=last.next
		last.next=new_node

	def print(self):
		current=self.head
		while(current):
			print(current.data,end="->")
			current=current.next
		print("None")

	def reverse(self):
		rll=linkedlist()
		current=self.head
		while(current):
			rll.prepend(current.data)
			current=current.next
		return rll


	def palindrome(self,other):
		ll=self.head
		rll=other.head
		while ll:
			if ll.data==rll.data:
				ll=ll.next
				rll=rll.next
			else:
				return False
				
		return True


		# current=self.head
		# last=self.head
		# count=0
		# A=[]
		# while last.next:
		# 	A.append(last.data)
		# 	last=last.next
		# 	count+=1
		# A.append(last.data)
		# print(A)
		# for i in range(len(A)-1,len(A)//2-1,-1):
		# 	print("i:",i)
		# 	print("currentdata",current.data)
		# 	if current.data!=A[i]:
		# 		return False
		# 	current=current.next
		# return True

inp=input("enter elements of linkedlist seperated by spaces")
Arr=list(map(int,inp.split()))

ll=linkedlist()
for i in Arr:
	ll.append(i)
ll.print()
rll=ll.reverse()
print(ll.palindrome(rll))




