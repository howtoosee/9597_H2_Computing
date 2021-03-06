def Binary_Search_Iterative(array, target):
	low, high =  0, len(array)-1

	while low <= high:
		mid = (low + high) // 2			# choose pivot to be in the middle
		pivot = array[mid]

		if pivot == target:				# target found
			return mid					# return array index

		elif target < pivot:			# target in lower subarray
			high = mid - 1				# adjust pointer

		else:							# target in higher subarray
			low = mid + 1				# adjust pointer

	if low > high:						# pointers cross -- target not found
		return -1						# return dummy value


def main():
	arr = [7, 19, 33, 57, 90, 100, 195, 299]
	target = 33

	pos = Binary_Search_Iterative(arr, target)
	if pos == -1:
		print("Target not found!")
	else:
		print("Number 33 is found at array index", pos)

main()
