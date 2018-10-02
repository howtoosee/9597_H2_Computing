class node:
	def __init__(self, data, next):
		self.data = data
		self.next = next


class linkedlist:
	def __init__(self, MAX):
		self.max = MAX
		self.root = 0
		self.nextfree = 1
		self.linked = [None] * (self.max + 1)

		for i in range(1, self.max):
			self.linked[i] = node("", i + 1)
		self.linked[self.max] = node("", 0)


	def add(self, value):
		if self.nextfree is 0:
			print("Linked list is full!")
			return ""

		else:
			target = self.nextfree
			self.linked[target].data = value
			self.nextfree = self.linked[target].next

			if self.root is 0:
				self.root = target
				self.linked[target].next = 0

			else:
				curr = self.root
				prev = curr

				while curr is not 0 and value > self.linked[curr].data:
					prev = curr
					curr = self.linked[curr].next

				if curr is self.root:
					self.linked[target].next = self.root
					self.root = target

				else:
					self.linked[prev].next = target
					self.linked[target].next = curr


	def display(self):
		print("Root:", self.root)
		print("Next free:", self.nextfree)
		print("Printing in index order:")

		print("{:<10}{:<10}{:<10}".format("Index", "Data", "Next"))

		for i in range(1, self.max + 1):
			data = self.linked[i].data
			next = self.linked[i].next
			print("{:<10}{:<10}{:<10}".format(i, data, next))


	def traverse(self):
		print("Traversing in order:")

		curr = self.root

		while curr is not 0:
			print(self.linked[curr].data, end = " ")
			curr = self.linked[curr].next

		print()

def main():
	mylist = linkedlist(10)

	values = ["m", "k", "j", "a", "x"]
	for value in values:
		mylist.add(value)

	mylist.display()
	mylist.traverse()

main()
