''''
2/26/2024
This script illustrates a simple doubly linked list
Herbe Chun
'''

class node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.before = None
	
class tree:
	def __init__(self):
		self.head = None
		
	def link(self, val):
		if self.head is None:
			newNode = node(val)
			newNode.next = None
			newNode.before = None
			self.head = newNode
		else:
			ptr = self.head
			newNode = node(val)
			while ptr.next is not None:
				ptr = ptr.next
			ptr.next = newNode
			newNode.before = ptr
			newNode.next = None
	
	def ptree(self):
		ptr = self.head
		print("foward")
		while (ptr is not None):
			print(ptr.val)
			ptr = ptr.next
		
		print("random")
		ptr = self.head
		print(ptr.val)
		ptr = ptr.next
		print(ptr.val)
		ptr = ptr.before
		print(ptr.val)
		
		print("backwards")
		ptr = self.head
		while (ptr.next is not None):
			ptr = ptr.next
		while (ptr is not None):
			print(ptr.val)
			ptr = ptr.before
		print()
		
class main():
	t1 = tree()
	t1.link(1)
	t1.link(2)
	t1.link(3)
	t1.ptree()

if "__init__" == "__main__":
	main()