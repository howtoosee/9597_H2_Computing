class node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right


class tree:
	def __init__(self, MAX):
		self.max = MAX
		self.root = 0
		self.nextfree = 1
		self.tree = [None] * (self.max + 1)

		for i in range(1, self.max):
			self.tree[i] = node("", 0, i + 1)
		self.tree[self.max] = node("", 0, 0)


	def add_iterative(self, value):
		if self.nextfree is 0:								# tree is full
			print("Tree is full!")
			return
		else:
			target = self.nextfree
			self.tree[target].data = value

			if self.root is 0:								# tree is empty
				self.root = target
				return ""

			else:											# tree is not empty
				curr = self.root
				prev = curr
				last = ""

				while curr is not 0:
					prev = curr

					if value < self.tree[curr].data:		# move left
						last = "L"
						curr = self.tree[curr].left
					else:									# move right
						last = "R"
						curr = self.tree[curr].right

				if last is "L":								# change pointer of prev node
					self.tree[prev].left = target
				else:
					self.tree[prev].right = target

			self.nextfree = self.tree[target].right			# update next free
			self.tree[target].right = 0						# update curr node's right ptr


	def add_recursive(self, value, curr):
		target = self.nextfree

		if self.root == 0:										# tree is empty
			self.root = target
			self.tree[target].data = value
			self.nextfree = self.tree[target].right
			self.tree[target].right = 0
			self.display()

			return ""

		else:													# tree is not empty
			curr_node = self.tree[curr]							# assign pointer

			if value < curr_node.data:							# compare values
				if curr_node.left != 0:							# curr_node.left is not empty
					self.add_recursive(value, curr_node.left)	# moves left

				else:											# curr_node.left is empty
					curr_node.left = target						# insert
					self.tree[target].data = value
					self.nextfree = self.tree[target].right
					self.tree[target].right = 0

			else:												# compare values
				if curr_node.right != 0:						# curr_node.right is not empty
					self.add_recursive(value, curr_node.right)	# moves right

				else:											# curr_node.right is empty
					curr_node.right = target					# insert
					self.tree[target].data = value
					self.nextfree = self.tree[target].right
					self.tree[target].right = 0


	def display(self):
		print("Root:", self.root)
		print("Next free:", self.nextfree)
		print("{:<10}{:<10}{:<10}{:<10}".format("Index", "Left", "Data", "Right"))
		for i in range(1, self.max + 1):
			left = self.tree[i].left
			data = self.tree[i].data
			right = self.tree[i].right

			print("{:<10}{:<10}{:<10}{:<10}".format(i, left, data, right))


	def inorder(self):
		if self.root is 0:
			print("Tree is empty!")
		else:
			print("Displaying in order:")
			self.traverseinorder(self.root)
			print()


	def traverseinorder(self, root):
		if root is not 0:
			self.traverseinorder(self.tree[root].left)
			print(self.tree[root].data, end = " ")
			self.traverseinorder(self.tree[root].right)


	def getroot(self):
		return self.root


	def getnextfree(self):
		return self.nextfree


def main():

	values = ["x", "m", "j", "o", "k"]

	'''
	mytree = tree(10)

	for value in values:
		mytree.add(value)
	mytree.display()
	mytree.inorder()
	'''


	mytree2 = tree(10)
	root = mytree2.getroot()
	nextfree = mytree2.getnextfree()
	if nextfree == 0:
		print("tree is full")
	else:
		for value in values:
			mytree2.add_recursive(value, root)
		mytree2.display()
		mytree2.inorder()

main()
