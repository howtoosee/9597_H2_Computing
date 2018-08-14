# collision method: linear probing

# hash function will be given
# for this example, i will hash the ascii value of given character


def GetPosition(hash_table, value):
	position = ord(value) % len(hash_table)				# get original position for given value

	return position


def AddItem(array, target):
	original_pos = GetPosition(array, target)			# get hashing position

	if array[original_pos] == None:						# hashed original_position is empty
		array[original_pos] = target					# assign target to position

		return array

	pos = (original_pos + 1) % len(array)				# get new hashing position
	while pos != original_pos:							# check for collision
		if array[pos] == None:							# empty location found
			array[pos] = target
			return array

		else:
			pos = (pos + 1) % len(array)				# increment position

	return -1											# array is full


def Search(array, target):
	original_pos = GetPosition(array, target)			# get hashing position
	
	if array[original_pos] == target:					# target found at original hashing position
		return original_pos

	pos = (original_pos + 1) % len(array)
	while pos != original_pos:
		if array[pos] == None:							# empty hashed position --> not found
			return -1

		elif array[pos] == target:						# target found
			return pos

		else:											# increment position
			pos = (pos + 1) % len(hash_table)

	return -1											# target not found


def main():
	hash_table = [None] * 11

	add_items = ["a", "k", "g", "c", "d", "z", "n", "x"]
	
	for item in add_items:
		if hash_table != -1:
			hash_table = AddItem(hash_table, item)

	print(hash_table)

	pos = Search(hash_table, "d")
	
	print("Letter 'd' is found at array index", pos)
		

main()