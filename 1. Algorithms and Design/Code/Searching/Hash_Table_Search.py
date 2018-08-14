# hash function will be given
# for this example, i will hash the ascii value of given character by taking modulo 11


def GetPosition(value):
	position = ord(value) % 11					# get original position for given value

	return position


def AddItem(hash_table, target):
	original_pos = GetPosition(target)			# get hashing position
	pos = original_pos

	while hash_table[pos] != "":				# check for collision
		if pos != original_pos:
			pos = (pos + 1) % 11				# increment position
		else:									# hash table is full
			return -1


	hash_table[pos] = target					# assign target to position

	return hash_table

'''
def Search(array, target):
	original_pos = GetPosition(target)			# get hashing position
	pos = original_pos

	found = False

	while not found:

		if array[pos] == None:					# target not at hashed position --> not found
			return -1

		elif array[pos] != target:				# increment position
			pos = (pos + 1) % 11

		else:
			return pos
'''

def main():
	hash_table = [""] * 11

	add_items = ["a", "k", "g", "c", "d", "z", "n", "x"]
	
	for item in add_items:
		if hash_table != -1:
			hash_table = AddItem(hash_table, item)

	print(hash_table)


main()