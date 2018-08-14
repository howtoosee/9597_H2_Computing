# collision method: chaining

# hash function will be given
# for this example, i will hash the ascii value of given character


def GetPosition(hash_table, value):
	position = ord(value) % len(hash_table)		# get original position for given value

	return position


def AddItem(array, target):
	pos = GetPosition(array, target)

	if array[pos] == []:
		array[pos] = [target]
	else:
		array[pos].append(target)

	return array


def Search(array, target):
	pos = GetPosition(array, target)

	if target in array[pos]:
		return pos

	else:
		return -1


def main():
	hash_table = [ [] ] * 11

	add_items = ["a", "k", "g", "c", "d", "z", "n", "x"]
	
	for item in add_items:
			hash_table = AddItem(hash_table, item)

	for element in hash_table:
		print(element)


	pos = Search(hash_table, "d")
	
	print("Letter 'd' is found at array index", pos)


main()
