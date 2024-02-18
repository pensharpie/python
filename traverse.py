'''
2/18/2024
Btree in Python illustrating pre, post and inorder traversal
Herbe Chun
'''

class tree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def add(self, val):
		if self.val is None:
			self.val = val
		else:
			if val < self.val:
				if self.left is None:
					self.left = tree(val)
				else:
					self.left.add(val)
			else: 
				if val > self.val:
					if self.right is None:
						self.right = tree(val)
					else:
						self.right.add(val)

'''
inorder: left, root, right
preorder: left, right, root
postorder: root, left, right
'''
def inorder(ptr):
	if (ptr == None):
		return
	inorder(ptr.left)
	print(ptr.val)
	inorder(ptr.right)
	
def preorder(ptr):
	if (ptr == None):
		return
	preorder(ptr.left)
	preorder(ptr.right)
	print(ptr.val)

def postorder(ptr):
	if (ptr == None):
		return
	print(ptr.val)
	postorder(ptr.left)
	postorder(ptr.right)
					
def main():
	t1 = tree(2)
	t1.add(3)
	t1.add(4)
	t1.add(5)
	t1.add(6)
	t1.add(7)
	t1.add(8)
	inorder(t1)
	print()
	preorder(t1)
	print()
	postorder(t1)
	
	
if __name__ == "__main__":
	main()