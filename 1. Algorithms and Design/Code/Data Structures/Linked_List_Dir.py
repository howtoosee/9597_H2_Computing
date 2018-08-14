class node:
	def __init__(self, value):
		self.value = value
		self.ptr = None


class linkedlist:
	def __init__(self):
		self.start = None

	def add(self, value):
		print("Adding '{}'.".format(value))

		if self.start is None:
			self.start = node(value)
			return ""

		else:
			curr = self.start
			prev = None

			while curr is not None and value > curr.value:
				prev = curr
				curr = curr.ptr

			newnode = node(value)
			if prev is None:
				newnode.ptr = self.start
				self.start = newnode
			else:
				newnode.ptr = prev.ptr
				prev.ptr = newnode


	def remove(self, value):
		if self.start is None:
			print("Linked list is empty!")
			return ""

		print("Removing '{}'.".format(value))

		curr = self.start
		prev = None
		while curr is not None and curr.value != value:
			prev = curr
			curr = curr.ptr

		if curr is None:
			print("Given value is not found!")
			return ""

		if prev is None:
			self.start = curr.ptr
		else:
			prev.ptr = curr.ptr



	def display(self):
		if self.start is None:
			print("Linked list is empty!")
			return ""
		else:
			print("Displaying linked list in order:")
			curr = self.start
			while curr is not None:
				print(curr.value)
				curr = curr.ptr


def main():
	MyList = linkedlist()

	values = ("N", "L", "O", "A", "X")
	for value in values:
		MyList.add(value)
	MyList.display()
	MyList.remove("O")
	MyList.display()

main()
