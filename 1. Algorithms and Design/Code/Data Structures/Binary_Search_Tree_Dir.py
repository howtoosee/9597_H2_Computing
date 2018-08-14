class node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class tree:
	def __init__(self, MAX):
		self.root = None
		self.max = MAX
		self.size = 0


	def add(self, value):
		if self.size is self.max:
			print("Tree is full!")
			return ""

		else:
			if self.root is None:
				self.root = node(value)
				return ""

			else:
				curr = self.root
				prev = curr
				last = ""

				while curr is not None:
					prev = curr

					if value < curr.data:
						last = "L"
						curr = curr.left
					else:
						last = "R"
						curr = curr.right

				if last is "L":
					prev.left = node(value)
				else:
					prev.right = node(value)


	def add_rec(self, tree, value):
		if tree is None:
			return node(value)

		if value < tree.data:
			if tree.left is None:
				tree.left = node(value)
			else:
				self.add_rec(tree.left, value)
		else:
			if tree.right is None:
				tree.right = node(value)
			else:
				self.add_rec(tree.right, value)


	def inorder(self):
		if self.root is 0:
			print("Tree is empty!")
		else:
			print("Displaying in order:")
			self.traverseinorder(self.root)
			print()


	def traverseinorder(self, root):
		if root is not None:
			self.traverseinorder(root.left)
			print(root.data, end = " ")
			self.traverseinorder(root.right)


def main():
	mytree = tree(10)

	values = ["x", "m", "j", "o", "k"]

	for value in values:
		mytree.add(value)

	mytree.inorder()

main()
