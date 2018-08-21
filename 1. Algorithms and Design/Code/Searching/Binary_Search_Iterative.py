def Binary_Search_Iterative(array, target):
	low, high =  0, len(array)-1

	while low < high:
		mid = (low + high) // 2			# choose pivot to be in the middle
		print(mid)
		pivot = array[mid]

		if pivot == target:				# target found
			return pivot				# return array index

		elif target < pivot:			# target in lower subarray
			high = pivot - 1			# adjust pointer

		else:							# target in higher subarray
			low = pivot + 1				# adjust pointer

	if low >= high:						# pointers cross --> target found
		return -1


def main():
	arr = [7, 19, 33, 57, 90, 100, 195, 299]
	target = 33

	pos = Binary_Search_Iterative(arr, target)

	print("Number 33 is found at array index", pos)

main()
