mydict =  {'carl':40, 'alan':2, 'bob':1, 'danny':3, "mike": 6}

def basics():
	value = "d"
	if mydict.get(value):
		print("Found")
	else:
		print("{} is not found".format(value))
	print()

	print("Displaying all keys:")
	for k in mydict.keys():
		print(k)
	print()


	print("Displaying all values:")
	for v in mydict.values():
		print(v)
	print()


	print("Displaying all keys and values:")
	for k, v in mydict.items():
		print(k, v)
	print()


	print("Delete the key 'mike':")
	mydict.pop("mike")
	print(mydict)
	print()

# Dictionaries are not sorted automatically.
def sort_auto():

	# sort by key
	sorted_element_key = []
	print("Sort automatically by key:")
	for key in sorted(mydict.keys()):
		sorted_element_key.append([key, mydict[key]])

	for element in sorted_element_key:
		k, v = element
		print(k, v)

	print()


	# sort by value
	sorted_elements_val = []
	print("Sort automatically by value:")
	for k, v in mydict.items():
		sorted_elements_val.append([k, v])
	sorted_elements_val.sort(key = lambda x: x[1])

	for element in sorted_elements_val:
		k, v = element
		print(k, v)

	print()


def sort_manual():
	print("Sorting manually by key:")

	sorted_elements = []

	while len(mydict.keys()) is not 0:
		smallest_key = None
		smallest_val = None

		for k, v in mydict.items():
			if smallest_key is None or smallest_val is None:
				smallest_key = k
				smallest_val = v
			if k < smallest_key:
				smallest_key = k
				smallest_val = v

		sorted_elements.append([smallest_key, smallest_val])
		mydict.pop(smallest_key)

	for element in sorted_elements:
		k, v = element
		print(k, v)


def main():
	basics()
	sort_auto()
	sort_manual()

main()
