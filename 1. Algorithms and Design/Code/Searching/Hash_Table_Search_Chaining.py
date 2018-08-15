# collision method: chaining

# hash function will be given
# for this example, i will hash the ascii value of given character


def GetPosition(hash_table, value):
	position = ord(value) % len(hash_table)		# get hash value

	return position


def AddItem(array, target):
	pos = GetPosition(array, target)			# get original position for given value

	if array[pos] == []:						# position is initially empty
		array[pos] = [target]					# initialise first value

	else:										# position contains some value
		array[pos].append(target)				# append to chain

	return array


def Search(array, target):
	pos = GetPosition(array, target)			# get original position for given value

	if target in array[pos]:					# check if target is at position
		return pos

	else:
		return -1


def main():
	hash_table = [ [] ] * 11					# initialise 2D array as hash table

	add_items = ["a", "k", "g", "c", "d", "z", "n", "x"]

	for item in add_items:
			hash_table = AddItem(hash_table, item)

	for element in hash_table:
		print(element)


	pos = Search(hash_table, "d")

	print("Letter 'd' is found at array index", pos)


main()
