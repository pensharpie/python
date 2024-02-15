''''
2/25/2024
This script illustrates a stack which features enque, dequeue and peek.
Herbe Chun
'''

class node:
	def __init__(self, val):
		self.val = val
		self.next = None
	
class list():
	def __init__(self):
		self.head = None;
		
	def enque(self, val):
		if self.head is None:
			self.head = node(val)
		else: 
			tail = self.head
			while tail.next is not None:
				tail = tail.next
			tail.next = node(val)

	def dequeue(self):
		if self.head is None:
			return
		else:
			self.head = self.head.next

	def printl(self):
		tail = self.head
		while tail.next is not None:
			print(tail.val)
			tail = tail.next
		print(tail.val)
		print()

	def peek(self):
		return(self.head.val)
			
class main():
    n1 = list()
    n1.enque(1)
    n1.enque(2)
    n1.enque(3)
    n1.printl()
    n1.dequeue()
    n1.printl()
    n1.dequeue()
    n1.printl()
    print(n1.peek())
    
if "__init__" == "__main__":
	main()
		