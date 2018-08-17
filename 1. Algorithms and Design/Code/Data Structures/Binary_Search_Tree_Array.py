class node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right


class tree:
	def __init__(self, MAX):
		self.max = MAX
		self.root = None
		self.nextfree = 1
		self.tree = [None] * (self.max + 1)

		for i in range(1, self.max):
			self.tree[i] = node("", 0, i + 1)
		self.tree[self.max] = node("", 0, 0)


	def add_iterative(self, value):
		if self.nextfree is 0:
			print("Tree is full!")
			return
		else:
			target = self.nextfree
			self.tree[target].data = value

			if self.root is None:
				self.root = target

			else:
				curr = self.root
				prev = curr
				last = ""

				while curr is not 0:
					prev = curr

					if value < self.tree[curr].data:
						last = "L"
						curr = self.tree[curr].left
					else:
						last = "R"
						curr = self.tree[curr].right

				if last is "L":
					self.tree[prev].left = target
				else:
					self.tree[prev].right = target

			self.nextfree = self.tree[target].right
			self.tree[target].right = 0


	def add_recursive(self, value, )


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


def main():

	values = ["x", "m", "j", "o", "k"]
	
	mytree = tree(10)



	for value in values:
		mytree.add(value)

	mytree.display()
	mytree.inorder()


	mytree2 = tree(10)

main()
