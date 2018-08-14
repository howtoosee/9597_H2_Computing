def Binary_Search_Recursive(array, target, low, high):

	pivot = (low + high) // 2			# choose pivot to be in the middle

	if array[pivot] == target:		# target found
		return pivot					# return array index

	elif target < array[pivot]:		# target in lower subarray
		return Binary_Search_Recursive(array, target, low, pivot - 1)	
									# recursively call search for lower subarray

	else:							# target in higher subarray
		return Binary_Search_Recursive(array, target, pivot + 1, high)
									# recursively call search for higher subarray

	if low >= high:					# pointers cross --> target not found
		return -1


def main():
	arr = [7, 19, 33, 57, 90, 100, 195, 299]
	target = 33

	print(Binary_Search_Recursive(arr, target, 0, len(arr)))


main()