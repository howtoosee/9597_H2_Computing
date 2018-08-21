def Binary_Search_Recursive(array, target, low, high):

	mid = (low + high) // 2			# choose pivot value to be in the middle
	pivot = array[mid]

	if pivot == target:				# target found
		return mid					# return array index

	elif target < pivot:			# target in lower subarray
		return Binary_Search_Recursive(array, target, low, mid - 1)
									# recursively call search for lower subarray

	else:							# target in higher subarray
		return Binary_Search_Recursive(array, target, mid + 1, high)
									# recursively call search for higher subarray

	if low > high:					# pointers cross --> target not found
		return -1


def main():
	arr = [7, 19, 33, 57, 90, 100, 195, 299]
	target = 33

	pos = Binary_Search_Recursive(arr, target, 0, len(arr))

	print("Number 33 is found at array index", pos)


main()
